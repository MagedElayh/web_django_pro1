from django import forms
from .models import Doctor, Period, Month ,Secertary
# import NumberInput
from django.forms import TimeInput
import datetime


class DoctorForm(forms.ModelForm):
    active = forms.BooleanField(initial=False)#this is no field add it
    class Meta:
        model = Doctor
        fields = '__all__'

class PeriodForm(forms.ModelForm):

    time_to=forms.TimeInput(attrs={'type': 'time'})
    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    birth_year1 = forms.DateField(widget=forms.SelectDateWidget())#this is no field
    # birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    day = forms.DateField(initial=datetime.date.today)
    #time_from=forms.TimeField(widget=forms.SplitTimeField(),required=True)
    doctor=forms.ModelChoiceField(
        queryset = Doctor.objects.all(),
        initial = 0
        )
    class Meta:
        model=Period
        fields='__all__'


class SecertaryForm(forms.ModelForm):
    class Meta:
        model : Secertary
        fields = '__all__'