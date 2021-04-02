from django.urls import path
from django.conf.urls import url
from Note_Test import views

urlpatterns = [
    path(r'',views.home,name ="note"),
]