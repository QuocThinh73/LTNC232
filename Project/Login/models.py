from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class MyUser(AbstractUser):
     USER_TYPE_CHOICES = [
         ('Student', "Student"),
         ('Teacher', 'Teacher'),
     ] 
     user_type = models.CharField(max_length = 20, choices = USER_TYPE_CHOICES)

class StudentUser(MyUser):
    student_id = models.CharField(max_length=30)
    score = models.FloatField(default = 0.0)
    date_of_birth = models.DateField(null = True, blank = True)
    major = models.CharField(max_length = 50, null = True, blank = True)

class TeacherUser(MyUser):
    teacher_id = models.CharField(max_length=30)