from django.views import View
from onlineapp.models import College
from django.shortcuts import *
from onlineapp.forms import AddCollege
from django.urls import resolve
from django.contrib.auth.mixins import LoginRequiredMixin


class AddCollegeView(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self,request,*args,**kwargs):
        if kwargs:
            college=College.objects.get(**kwargs)
            form=AddCollege(instance=college)
        else:
            form = AddCollege()

        return render(
            request,
            template_name='addcollege.html',
            context={
                'form': form,
                'title': 'add_new_college'
            }
        )

    def post(self,request,*args,**kwargs):
        if resolve(request.path_info).url_name=='delete_college_html':
            College.objects.get(pk=kwargs.get('pk')).delete()
            return redirect('colleges_html')

        if resolve(request.path_info).url_name=='edit_college_html':
            college=College.objects.get(pk=kwargs.get('pk'))
            form=AddCollege(request.POST,instance=college)
        else:
            form=AddCollege(request.POST)

        if form.is_valid():
            form.save()
            return redirect('colleges_html')

        return render(
            request,
            template_name='addcollege.html',
            context={
                'form': form,
                'title': 'add_new_college'
            }
        )
