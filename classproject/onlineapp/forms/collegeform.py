from django import forms

from onlineapp.models import College


class AddCollege(forms.ModelForm):
    class Meta:
        model=College
        exclude=['id']
        widgets={
            'name':forms.TextInput(attrs={'class':'input box is-rounded is-primary','placeholder':'enter the name'}),
            'acronym':forms.TextInput(attrs={'class':'input box is-rounded is-primary','placeholder':'enter the acronym'}),
            'location':forms.TextInput(attrs={'class':'input box is-rounded is-primary','placeholder':'enter the location'}),
            'contact':forms.EmailInput(attrs={'class':'input box is-rounded is-primary','placeholder':'enter the contact'})
        }