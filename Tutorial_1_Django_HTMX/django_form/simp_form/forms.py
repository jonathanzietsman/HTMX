from django import forms

class SampleForm(forms.Form):
    name = forms.CharField(min_length=3)
    email = forms.EmailField()
    favourite_color = forms.CharField()
