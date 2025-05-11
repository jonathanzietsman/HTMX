from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'address', 'notes']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'John Doe',
                'minlength': '2',
                'maxlength': '100',
                'pattern': r'^[a-zA-Z\s\-\.]{2,100}$',
                'title': 'Name must be 2-100 characters long and can only contain letters, spaces, hyphens, and periods.'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'john.doe@example.com',
                'maxlength': '254'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': '+1234567890',
                'pattern': r'^\+?1?\d{9,15}$',
                'title': 'Phone number must be entered in the format: +999999999. Up to 15 digits allowed.'
            }),
            'address': forms.Textarea(attrs={
                'rows': 3,
                'maxlength': '500',
                'placeholder': 'Enter the contact\'s address (optional)'
            }),
            'notes': forms.Textarea(attrs={
                'rows': 3,
                'maxlength': '1000',
                'placeholder': 'Enter any additional notes (optional)'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('name', css_class='form-control'),
            Field('email', css_class='form-control'),
            Field('phone', css_class='form-control'),
            Field('address', css_class='form-control'),
            Field('notes', css_class='form-control'),
            Submit('submit', 'Save Contact', css_class='btn btn-primary mt-3')
        ) 