from django import forms
from .models import FbModel


class FbForm(forms.ModelForm):
    name = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder":"Enter name"}))
    feedback = forms.CharField(label="", widget=forms.Textarea(attrs={"placeholder":"Enter feedback here", 
    "cols":"22", "rows":"5", "style":"resize:none"}))
    class Meta:
        model = FbModel
        fields = ("name", "feedback")
        