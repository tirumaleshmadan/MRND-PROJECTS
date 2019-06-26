from django.contrib import admin
from django.urls import path
from onlineapp.views import *


urlpatterns=[


    path("",lambda req :redirect('colleges_html')),

    path('colleges/',CollegeView.as_view(),name='colleges_html'),
    path('colleges/<int:pk>/',CollegeView.as_view(),name='collegedetails_html'),


    path('colleges/add/',AddCollegeView.as_view(),name='add_college_html'),
    path('colleges/<int:pk>/edit/',AddCollegeView.as_view(),name='edit_college_html'),
    path('colleges/<int:pk>/delete/',AddCollegeView.as_view(),name='delete_college_html'),

    path('colleges/<int:pk>/add/',AddStudentView.as_view(),name='add_student_html'),
    path('colleges/<int:pk>/<int:sk>/edit/',AddStudentView.as_view(),name='edit_student_html'),
    path('colleges/<int:pk>/<int:sk>/delete/',AddStudentView.as_view(),name='delete_student_html'),

    path('login/',LoginView.as_view(),name='login_html'),
    path('signup/',SighupView.as_view(),name='signup_html'),
    path('logout/',LogoutView.as_view(),name='logout_html')

]