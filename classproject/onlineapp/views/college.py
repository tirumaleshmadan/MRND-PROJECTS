from django.views import View
from onlineapp.models import College,Student
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin


class CollegeView(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self,request,*args,**kwargs):
        if kwargs:
            college=College.objects.get(**kwargs)
            students=list(college.student_set.order_by('-mocktest1__total'))
            return render(
                request,
                template_name='college_details.html',
                context={
                    'college':college,
                    'students':students,
                    'title':college.name.upper(),
                    'user_permissions':request.user.user_permissions
                }
            )
        colleges=College.objects.all()
        return render(
            request,
            template_name='colleges.html',
            context={
                'jails':colleges,
                'title':'COLLEGES',
                'user_permissions': request.user.user_permissions
            }
        )