from mainpage import views
from django.urls import path

urlpatterns = [
    path(r'',views.mainpage,name="mainpage"),   
    path('doctor/',views.doctor,name="doctor"),
    path('add_doctor/',views.DoctorView.as_view(),name="adddoctor"),
    path('period/',views.PeriodView.as_view(),name="period"),
    path('table/',views.TableView.as_view(),name="table"),
    path('secertary/',views.SecertaryView.as_view(),name="secertary"), 
    path('doctor_list/',views.DoctorList.as_view(),name="doctor_list"),
    path('doctor_list/<int:pk>/',views.DoctorDetail.as_view(),name="doctor_detail"),
    path('doctor/<int:pk>/',views.DoctorDetail.as_view(),name="doctor_detail"),
]
