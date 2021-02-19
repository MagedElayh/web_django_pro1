from __future__ import unicode_literals

from django.db import models


class Book(models.Model):
    frist_name=models.CharField("Doctor's first name",max_length=20,blank=False)
    last_name = models.CharField("Doctor's last name",max_length=20,blank=False)
    phone= models.PositiveIntegerField(blank=False, null=False)
    city=models.CharField(max_length=15,blank=True,null=True)
    country=models.CharField(max_length=15,blank=True,null=True)
    mail=models.EmailField("email", max_length=254)
    date_entry=models.DateField(
        "date entry", auto_now=False, auto_now_add=False,
        blank=True,null=True
    )
    #active=
    date_out=models.DateField("date entry", auto_now=False, auto_now_add=False,blank=True,null=True)

    def __str__(self):
        return self.frist_name

    # class Meta:
    #     ordering = ['frist_name']
    