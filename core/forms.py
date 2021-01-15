from django import forms
from django.core.mail.message import EmailMessage


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    subject = forms.CharField(label='subject', max_length=120)
    message = forms.CharField(label='message', widget=forms.Textarea())

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        content = f'Name: {name}\nE-mail: {email}\nSubject: {subject}\nmessage: {message}'
        mail = EmailMessage(
            subject=subject,
            body=content,
            from_email='contato@dominio.com.br',
            to=['contact@domain.com.br',],
            headers={'Reply-To': email}
        )
        mail.send()
