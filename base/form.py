from django import forms
from.models import test
class reviewform(forms.ModelForm):
    class Meta:
        model=test
        fields='__all__'