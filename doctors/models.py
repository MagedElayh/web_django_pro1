from __future__ import unicode_literals

from django.db import models


# class Book(models.Model):
#     HARDCOVER = 1
#     PAPERBACK = 2
#     EBOOK = 3
#     BOOK_TYPES = (
#         (HARDCOVER, 'Hardcover'),
#         (PAPERBACK, 'Paperback'),
#         (EBOOK, 'E-book'),
#     )
#     title = models.CharField(max_length=50)
#     publication_date = models.DateField(blank=True, null=True)
#     author = models.CharField(max_length=30, blank=True)
#     price = models.DecimalField(max_digits=5, decimal_places=2)
#     pages = models.IntegerField(blank=True, null=True)
#     book_type = models.PositiveSmallIntegerField(choices=BOOK_TYPES, blank=True, null=True)

class DoctorBook(models.Model):
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

    # def __str__(self):
    #     return self.frist_name

    # class Meta:
    #     ordering = ['frist_name']
    
