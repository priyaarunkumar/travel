from django import forms
from . models import place
class mform(forms.ModelForm):
    class meta:

        model=place

        fields=['name','desc','img']