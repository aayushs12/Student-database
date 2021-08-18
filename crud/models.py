from django.db import models
from django.db.models.deletion import CASCADE
class crudst(models.Model):
    stid=models.AutoField(primary_key=True)
    stname=models.CharField(max_length=70)
    stgrade=models.CharField(max_length=50)
    stemail=models.CharField(max_length=90,unique=True)
class course(models.Model):
    cid=models.CharField(max_length=50,primary_key=True)
    cname=models.CharField(max_length=70)
    credits=models.IntegerField()
class check(models.Model):
    studid=models.ForeignKey(crudst,on_delete=CASCADE)
    courseid=models.ForeignKey(course,on_delete=CASCADE)
class newp(models.Model):
    studentid=models.ForeignKey(crudst,on_delete=CASCADE)
    courseno=models.ForeignKey(course,on_delete=CASCADE)



