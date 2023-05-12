from django import forms
from .models import feedback, Contact

class feedbackForm(forms.ModelForm):
    class Meta:
        model = feedback
        fields = ['feedback_type','feedback']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']