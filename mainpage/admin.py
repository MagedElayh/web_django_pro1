from django.contrib import admin
from mainpage.models import Doctor,Month,Period,Sanad,Section_of_Building,Sick,Secertary

# class PeriodInline(admin.StackedInline):
#     model = Period
#     extra = 3

# class DoctorAdmin(admin.ModelAdmin):
    
#     class Meta:
#         fields = '__all__'
#         inlines = [PeriodInline]
#     # fields = ['last_name','frist_name']
    

admin.site.register(Doctor)
admin.site.register(Period)
admin.site.register(Month)
admin.site.register(Sick)
admin.site.register(Sanad)
admin.site.register(Secertary)
admin.site.register(Section_of_Building)