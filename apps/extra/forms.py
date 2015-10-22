# -*- coding: utf-8 -*-
from django import forms
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings


class ContactForm(forms.Form):
    """ Contact form  """

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        self.fields['name'].error_messages = {'required': 'Field name is required.'}
        self.fields['email'].error_messages = {'required': 'Field email is required.'}
        self.fields['subject'].error_messages = {'required': 'Field subject is required.'}
        self.fields['phone'].error_messages = {'required': 'Field phone is required.'}
        self.fields['message'].error_messages = {'required': 'Field message is required.'}

    name = forms.CharField(
        label=u'Name',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'})
    )

    email = forms.EmailField(
        label='Email',
        max_length=75,
        widget=forms.TextInput(attrs={'placeholder': 'Email address', 'class': 'form-control'})
    )
    subject = forms.CharField(
        label=u'Subject',
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Subject', 'class': 'form-control'})
    )
    phone = forms.CharField(
        label=u'Phone',
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Phone', 'class': 'form-control'})
    )
    message = forms.CharField(
        label='Message',
        widget=forms.Textarea(attrs={'placeholder':'Your Message','class':'form-control','rows':4})
    )

    def send_mail(self):
        """
        Send contact mail to Mohamed
        """
        data = self.cleaned_data
        subject_txt = '[TRADE] : ' + data['subject'].strip()

        body_txt = render_to_string(
            'emails/contact/email_body.txt',
            {
                'sender': data['name'],
                'email': data['email'],
                'message': data['message'],
                'phone': data['phone'],
            }
        ).strip()

        email = EmailMessage(subject_txt, body_txt, data['email'], [settings.TO_EMAIL, ], [], )
        email.send()