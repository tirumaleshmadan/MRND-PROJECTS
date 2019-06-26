from django.views import View
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from onlineapp.forms import Login,Signup
from django.shortcuts import *



class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('login_html')


class LoginView(View):
    def get(self,request):
        login_form=Login()
        if request.user.is_authenticated:
            return redirect('colleges_html')
        return render(
            request,
            template_name='login.html',
            context={
                'login_form':login_form
            }
        )

    def post(self,request):
        login_form=Login(request.POST)
        if login_form.is_valid():
            user = authenticate(
                request,
                username=login_form.cleaned_data['username'],
                password=login_form.cleaned_data['password']
        )
        if user is not None:
            login(request,user)
            return redirect('colleges_html')
        else:
            messages.error(request,'INVALID LOGIN CREDENTIALS')

        return render(
            request,
            template_name='login.html',
            context={
                'login_form':login_form
            }
        )


class SighupView(View):
    def get(self,request):
        signup_form=Signup()
        return render(
            request,
            template_name='signup.html',
            context={
                'signup_form': signup_form
            }
        )

    def post(self,request):
        signup_form=Signup(request.POST)
        if signup_form.is_valid():
            user=User.objects.create_user(**signup_form.cleaned_data)
            user.save()

            if user is not None:
                login(request,user)
                return redirect('colleges_html')

        return render(
            request,
            template_name='signup_html',
            context={
                'signup_form':signup_form
            }
        )
