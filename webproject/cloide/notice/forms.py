from django import forms
from .models import Notice

class NoticeUpdate(forms.ModelForm):
    class Meta:            
        model = Notice
        fields = ['title', 'body']