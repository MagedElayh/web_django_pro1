from django import forms
from .models import COURSE,COURSE_SUBJECT,TEACHER,SUBJECT

class TeacherForm(forms.ModelForm):
    class Meta:
        model = TEACHER
        fields = '__all__'

class SubjectForm(forms.ModelForm):
    class Meta:
        model = SUBJECT
        fields = ['Subject_Code','Subject_Name',]










# from .models import Member


# class MemberForm(forms.ModelForm):
#     class Meta:
#         model = Member
#         fields = '__all__'