from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class Owner(models.Model):
    user_id = models.IntegerField(primary_key=True, verbose_name="工号")
    user_real_name = models.CharField(max_length=20, verbose_name="姓名")
    user_password = models.CharField(max_length=18, verbose_name="密码")
    user_type = models.CharField(max_length=20, verbose_name="权限")
    def __str__(self):
        return self.user.username

class Instructor(models.Model):
    class Meta:
        verbose_name_plural = "导员"
    user_id = models.ForeignKey(Owner,primary_key=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    contact = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name

class College(models.Model):
    class Meta:
        verbose_name_plural = "专业"
    name = models.CharField(max_length=20,primary_key=True)
    def __str__(self):
        return self.name

class Class(models.Model):
    class Meta:
        verbose_name_plural = "班级"
    name = models.CharField(max_length=20,primary_key=True)
    instructorid = models.ForeignKey(Instructor, null=True,on_delete=models.CASCADE)
    collegeid = models.ForeignKey(College, null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Building(models.Model):
    name = models.CharField(max_length=20,primary_key=True)
    amount = models.IntegerField(default=0, null=True)
    def __str__(self):
        return self.name

class Room(models.Model):
    name = models.CharField(max_length=20,primary_key=True)
    room_type = models.CharField(max_length=20, null=True)
    capacity = models.IntegerField(default=0, null=True)
    buildingid = models.ForeignKey(Building,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Student(models.Model):
    class Meta:
        verbose_name_plural = "学生"
    # sno = models.CharField(max_length=20, primary_key=True)
    # user = models.ForeignKey(Owner,on_delete=models.CASCADE)
    sno = models.ForeignKey(Owner,on_delete=models.CASCADE,primary_key=True)
    name = models.CharField(max_length=20)
    sex = models.NullBooleanField(null=True)
    classid = models.ForeignKey(Class, null=True,on_delete=models.CASCADE)
    roomid = models.ForeignKey(Room, null=True,on_delete=models.CASCADE)
    contact = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name


class Secretary(models.Model):
    class Meta:
        verbose_name_plural = "书记"
    user = models.ForeignKey(Owner,primary_key=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    contact = models.CharField(max_length=200, null=True)
    collegeid = models.ForeignKey(College,on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Housemaster(models.Model):
    class Meta:
        verbose_name_plural = "舍管"
    user = models.ForeignKey(Owner,primary_key=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    contact = models.CharField(max_length=200, null=True)
    buildingid = models.ForeignKey(Building, null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Mark(models.Model):
    class Meta:
        verbose_name_plural = "评分"
    roomid = models.ForeignKey(Room,primary_key=True,on_delete=models.CASCADE)
    dt = models.DateTimeField()
    score = models.FloatField()
    housemasterid = models.ForeignKey(Housemaster,on_delete=models.CASCADE)
    remark = models.TextField(null=True)
    class Meta:
        unique_together = ('roomid', 'dt')

class Fee(models.Model):
    class Meta:
        verbose_name_plural = "电费余额"
    roomid = models.ForeignKey(Room, primary_key=True,on_delete=models.CASCADE)
    remain = models.FloatField()

class FeeRecord(models.Model):
    roomid = models.ForeignKey(Room,primary_key=True,on_delete=models.CASCADE)
    dt = models.DateTimeField()
    amount = models.FloatField()
    class Meta:
        unique_together = ('roomid', 'dt')

class Maintenance(models.Model):
    user = models.ForeignKey(Owner,primary_key=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    contact = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name

class Repair(models.Model):
    item = models.CharField(max_length=20,primary_key=True)
    roomid = models.ForeignKey(Room,on_delete=models.CASCADE)
    book_dt = models.DateTimeField()
    reason = models.TextField(null=True)
    fix_dt = models.DateTimeField(null=True)
    maintenanceid = models.ForeignKey(Maintenance, null=True,on_delete=models.CASCADE)
    remark = models.TextField(null=True)
    class Meta:
        unique_together = ('item', 'roomid', 'book_dt')
    def __str__(self):
        return self.item

class QuitApply(models.Model):
    sno = models.ForeignKey(Student,primary_key=True,on_delete=models.CASCADE)
    roomid = models.ForeignKey(Room,on_delete=models.CASCADE)
    dt = models.DateTimeField()
    reason = models.TextField()
    housemaster_check = models.NullBooleanField(null=True)
    instructor_check = models.NullBooleanField(null=True)
    secretary_check = models.NullBooleanField(null=True)
    class Meta:
        unique_together = ('sno', 'roomid', 'dt')

class EnterApply(models.Model):
    sno = models.ForeignKey(Student,primary_key=True,on_delete=models.CASCADE)
    roomid = models.ForeignKey(Room,on_delete=models.CASCADE)
    dt = models.DateTimeField()
    housemaster_check = models.NullBooleanField(null=True)
    instructor_check = models.NullBooleanField(null=True)
    secretary_check = models.NullBooleanField(null=True)
    class Meta:
        unique_together = ('sno', 'roomid', 'dt')

class LiveRecord(models.Model):
    sno = models.ForeignKey(Student,primary_key=True,on_delete=models.CASCADE)
    roomid = models.ForeignKey(Room,on_delete=models.CASCADE)
    enter_time = models.DateTimeField()
    quit_time = models.DateTimeField(null=True)
    class Meta:
        unique_together = ('sno', 'roomid', 'enter_time')

class Visitor(models.Model):
    name = models.CharField(max_length=20,primary_key=True)
    sex = models.BooleanField()
    document_type = models.CharField(max_length=20, null=True)
    documentno = models.CharField(max_length=20, null=True)
    contact = models.CharField(max_length=200, null=True)
    dt = models.DateTimeField()
    housemasterid = models.ForeignKey(Housemaster,on_delete=models.CASCADE)
    def __str__(self):
        return self.name




