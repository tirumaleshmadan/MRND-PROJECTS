from django import forms

from onlineapp.models import Student,MockTest1


class AddStudent(forms.ModelForm):
    class Meta:
        model=Student
        exclude=['id','dob','db_folder','college']
        widgets={
            'name':forms.TextInput(attrs={'class':'input box is-rounded is-primary','placeholder':'enter the name'}),
            'email':forms.EmailInput(attrs={'class':'input box is-rounded is-primary','placeholder':'enter the email'}),
            'dropped_out':forms.CheckboxInput(attrs={'class':'checkbox'})
        }

class AddMarks(forms.ModelForm):
    class Meta:
        model=MockTest1
        exclude=['id','student']
        widgets={
            'problem1':forms.NumberInput(attrs={'class':'input box is-rounded is-primary','placeholder':'enter problem1 marks'}),
            'problem2': forms.NumberInput(attrs={'class': 'input box is-rounded is-primary', 'placeholder': 'enter problem2 marks'}),
            'problem3': forms.NumberInput(attrs={'class': 'input box is-rounded is-primary', 'placeholder': 'enter problem3 marks'}),
            'problem4': forms.NumberInput(attrs={'class': 'input box is-rounded is-primary', 'placeholder': 'enter problem4 marks'}),
            'total': forms.NumberInput(attrs={'class': 'input box is-rounded is-primary', 'placeholder': 'enter total marks'})
        }

