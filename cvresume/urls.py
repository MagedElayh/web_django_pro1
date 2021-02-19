"""cvresume URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path,include
# # from mainpage import views


# urlpatterns = [
#     path(r'admin/', admin.site.urls),
#     # path('',views.mainpage),
#     path(r'',include('books.urls')),
# ]

from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from django.views.generic import TemplateView

from books import views
from CRUDAPP import views as vcard
from myapp import views as vmyapp

urlpatterns = [
    # url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'admin/', admin.site.urls),
    url(r'',include('mainpage.urls')),
    url(r'^books/$', views.book_list, name='book_list'),
    url(r'^books/create/$', views.book_create, name='book_create'),
    url(r'^books/(?P<pk>\d+)/update/$', views.book_update, name='book_update'),
    url(r'^books/(?P<pk>\d+)/delete/$', views.book_delete, name='book_delete'),

    url('card/',vcard.HomePage,name="home"),
    url('card/insert_student', vcard.InsertStudent,name="insert"),
    url('card/update_all', vcard.update_all,name="update_all"),
    url('card/delete_data', vcard.delete_data,name="delete_data"),

    #        myapp    urls   
    path('myapp',vmyapp.index,name = 'maapp'),
    url(r'^create$', vmyapp.create, name='create'),
    url(r'^read$', vmyapp.read, name='read'),
    url(r'^edit/(?P<id>\d+)$', vmyapp.edit, name='edit'),
    url(r'^edit/update/(?P<id>\d+)$', vmyapp.update, name='update'),
    url(r'^delete/(?P<id>\d+)$', vmyapp.delete, name='delete'),
    url(r'^myapp/create/$', vmyapp.member_create, name='member_create'),

]
