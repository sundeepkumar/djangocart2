# sendemail/forms.py
from django import forms

class ContactForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea, required=True)