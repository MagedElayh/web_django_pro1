#models.py
from django.db import models
 
# # Create your models here.
# class Member(models.Model):
#     firstname = models.CharField(max_length=40)
#     lastname = models.CharField(max_length=40)
  
#     created = models.DateTimeField(auto_now_add=True)
  
#     def __str__(self):
#         return self.firstname + " " + self.lastname
 
#     class Meta:
#         ordering = ['created']
   
#     class Meta:  
#         db_table = "blog_member"

class COURSE(models.Model):
    Course_Name = models.CharField(max_length=100)

class TEACHER(models.Model):
    T_Code = models.CharField(max_length=100)
    FN = models.CharField(max_length=100)
    LN = models.CharField(max_length=100)
    Dept_Code = models.CharField(max_length=100)
    Ext = models.CharField(max_length=100)

class SUBJECT(models.Model):
    Subject_Code = models.CharField(max_length=100,primary_key=True)
    Subject_Name = models.CharField(max_length=100)
    T_Code = models.ForeignKey(TEACHER, on_delete=models.CASCADE,blank=True,null=True)

class COURSE_SUBJECT(models.Model):
    Course       = models.ForeignKey(COURSE, on_delete=models.CASCADE)
    Subject_Code = models.ForeignKey(SUBJECT, on_delete=models.CASCADE)
    Subject_Type = models.CharField(max_length=100)
    

# class OFFERING(models.Model):
#     StartDate = models.DateField(auto_now_add=False)
#     EndDate = models.DateField(auto_now_add=False)
#     Subject_Code = models.ForeignKey(SUBJECT, on_delete=models.CASCADE)


