from django import forms

from .models import DoctorBook


class DoctorBookForm(forms.ModelForm):
    class Meta:
        model = DoctorBook
        fields = '__all__'
