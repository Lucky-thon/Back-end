# board/forms.py
from django import forms
from .models import MissionSuccessPost

class MissionSuccessPostForm(forms.ModelForm):
    class Meta:
        model = MissionSuccessPost
        fields = ['title', 'content', 'image']
