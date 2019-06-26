from django import forms


class Login(forms.Form):
    username=forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class':'input box is-rounded is-primary','placeholder':'enter username'})
    )
    password=forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class':'input box is-rounded is-primary','placeholder':'enter password'})
    )

class Signup(forms.Form):
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'input box is-rounded is-primary', 'placeholder': 'enter first name'})
    )
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'input box is-rounded is-primary', 'placeholder': 'enter last name'})
    )
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'input box is-rounded is-primary', 'placeholder': 'enter username'})
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'input box is-rounded is-primary', 'placeholder': 'enter your password'})
    )