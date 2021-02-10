from django.db import models
from django.utils.translation import gettext_lazy as _
#from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Doctor(models.Model):
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

    class Meta:
        ordering = ['frist_name']
    

class Period(models.Model):
    time_from = models.TimeField("time period start", auto_now=False, auto_now_add=False)
    time_to   = models.TimeField("time period end", auto_now=False, auto_now_add=False)
    doctor    = models.ManyToManyField(Doctor)

    def __str__(self):
        return str(self.id)

class Month(models.Model):
    month_number = models.PositiveIntegerField("number of month",unique=True)
    days         = models.DateField(unique=True)
    period       = models.ManyToManyField(Period)
    # add models.ManyToManyField(Doctor)
    def __str__(self):
        return self.month_number

class Sick(models.Model):
    sex = [
        ('male', 'male'),
        ('female', 'female'),
        ('none', 'none'), 
    ]
    bloods=[
        ('O+','O+'),('O-','O-'),
        ('A+','A+'),('A-','A-'),
        ('B+','B+'),('B-','B-'),
        ('AB+','AB+'),('AB-','AB-'),
        ('none','null'),
    ]
    frist_name = models.CharField("Sick's first name",max_length=20,blank=False)
    mid_name   = models.CharField("Sick's middle name",max_length=20,blank=True)
    last_name  = models.CharField("Sick's last name",max_length=20,blank=False)
    #phone= models.PositiveIntegerField(blank=False, null=False)
    mail       = models.EmailField("email", max_length=254)
    # phone=models.PhoneNumberField("phone",max_length=20)
    old        = models.CharField("old",max_length=20,blank=True)
    sex = models.CharField(
        max_length=10,
        choices=sex,
        default='none',
        )
    blood=models.CharField(
        "blood",max_length=5,
        choices=bloods,
        default='none')
    note=models.CharField("note",max_length=300,blank=True, null=False)
    sanads = models.ManyToManyField(Doctor, through='Sanad')
    # sanad = models.ManyToManyField(Doctor)
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Sanad(models.Model):
    get_date=models.DateField("date entry", auto_now_add=True)
    values=models.CharField(max_length=10)
    note=models.CharField("note",max_length=300,blank=True, null=True)
    sick=models.ForeignKey(Sick, on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __unicode__(self):
        return u' value:  %s'%(self.values)

class Section_of_Building(models.Model):
    name    = models.CharField(max_length=250, blank=False, null=False)
    position = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.name

class Secertary(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    #phone=models.PhoneNumberField(blank=True)
    phone= models.CharField(max_length=20, blank=True, null=True)
    mail=models.EmailField(max_length=50,blank=True,null=True)
    country = models.CharField(max_length=40, blank=True, null=True)
    active =models.BooleanField(default=False)
    other=models.TextField(blank=True, null=True)
    sex=models.CharField(max_length=8, blank=True, null=True)
    dateEntry=models.DateField(auto_now=True,auto_now_add=False)


