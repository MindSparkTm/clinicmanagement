from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'message_no', 'subject', 'body', 'sender_archived', 'recipient_archived', 'sender']


