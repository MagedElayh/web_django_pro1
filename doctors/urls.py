from django.conf.urls import url, include
from django.views.generic import TemplateView

from doctors import views

urlpatterns = [
    # url(r'', TemplateView.as_view(template_name='home.html'), name='home'),
    
    url(r'book/', views.doctor_list, name='book_list'),
    url(r'book/create/', views.doctor_create, name='book_create'),
    url(r'book/(?P<pk>\d+)/update/', views.doctor_update, name='book_update'),
    url(r'book/(?P<pk>\d+)/delete/', views.doctor_delete, name='book_delete'),
]