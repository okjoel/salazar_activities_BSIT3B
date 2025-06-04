from django.db import models

class Institution(models.Model):
    name = models.CharField(max_length=100)
    # add other fields as needed

class Student(models.Model):
    name = models.CharField(max_length=100)
    # add other fields as needed

class Credential(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    degree = models.CharField(max_length=100)
    issue_date = models.DateField()
    # add other fields as needed
