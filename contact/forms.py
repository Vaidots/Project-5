from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Name'}),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email'}),
    )
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Subject'}),
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Please enter your message'}),
    )

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
