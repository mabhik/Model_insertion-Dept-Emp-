from django.db import models

# Create your models here.

class Emp(models.Model):
    Empno=models.IntegerField(primary_key=True)
    Ename=models.CharField(max_length=20)
    Deptno=models.IntegerField()

    def __str__(self):
        return self.Deptno

class Dept(models.Model):
    Deptno=models.ForeignKey(Emp, on_delete=models.CASCADE)
    Loc=models.CharField(max_length=20)
    