from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_name=models.CharField(max_length=20)
    student_age=models.IntegerField()
    student_date_birth=models.DateField()
    student_email=models.EmailField()
    student_address=models.TextField()
