from django.views import View
from onlineapp.models import Student,MockTest1
from django.shortcuts import *
from onlineapp.forms import *
from django.urls import *
from django.contrib.auth.mixins import LoginRequiredMixin


class AddStudentView(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self,request,*args,**kwargs):
        stud_form=AddStudent()
        marks_form=AddMarks()
        if len(kwargs)==2:
            student = Student.objects.get(id=kwargs['sk'])
            mocktest = MockTest1.objects.get(student_id=student.id)
            stud_form = AddStudent(instance=student)
            marks_form = AddMarks(instance=mocktest)
        return render(
            request,
            template_name='addstudent.html',
            context={
                'student_form': stud_form,
                'marks_form':marks_form,
                'title':'add_new_student'
            }
        )

    def post(self,request,*args,**kwargs):
        if resolve(request.path_info).url_name=='delete_student_html':
            Student.objects.get(pk=kwargs.get('sk')).delete()
            return redirect('collegedetails_html',kwargs['pk'])

        if resolve(request.path_info).url_name == 'edit_student_html':
            student=Student.objects.get(id=kwargs['sk'])
            mocktest=MockTest1.objects.get(student_id=student.id)
            stud_form = AddStudent(request.POST,instance=student)
            marks_form = AddMarks(request.POST,instance=mocktest)

            if stud_form.is_valid() and marks_form.is_valid():
                stud_form.save()
                marks_form.save()
                return redirect('collegedetails_html', kwargs['pk'])


        stud_form=AddStudent(request.POST)
        marks_form=AddMarks(request.POST)
        if stud_form.is_valid() and marks_form.is_valid():
            stud_form=stud_form.save(commit=False)
            marks_form=marks_form.save(commit=False)
            stud_form.college=College.objects.get(id=kwargs['pk'])
            stud_form.save()
            marks_form.student=Student.objects.get(id=stud_form.id)
            marks_form.save()
            return redirect('collegedetails_html',kwargs['pk'])

        return render(
            request,
            template_name='addstudent.html',
            context={
                'student_form': stud_form,
                'marks_form': marks_form,
                'title': 'add_new_student'
            }
        )