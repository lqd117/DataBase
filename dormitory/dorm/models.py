from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class Owner(models.Model):
    class Meta:
        verbose_name_plural = "用户"
    user_id = models.IntegerField(primary_key=True, verbose_name="工号")
    user_real_name = models.CharField(max_length=20, verbose_name="姓名")
    user_password = models.CharField(max_length=18, verbose_name="密码")
    user_type = models.CharField(max_length=20, verbose_name="权限")

class Instructor(models.Model):
    class Meta:
        verbose_name_plural = "导员"
    user_id = models.ForeignKey(Owner,primary_key=True,on_delete=models.CASCADE,verbose_name='工号')
    name = models.CharField(max_length=20,verbose_name='姓名')
    contact = models.CharField(max_length=200, null=True,verbose_name='联系方式')
    def __str__(self):
        return self.name

class College(models.Model):
    class Meta:
        verbose_name_plural = "专业"
    name = models.CharField(max_length=20,primary_key=True,verbose_name='专业名')
    def __str__(self):
        return self.name

class Class(models.Model):
    class Meta:
        verbose_name_plural = "班级"
    name = models.CharField(max_length=20,primary_key=True,verbose_name='班级名')
    instructorid = models.ForeignKey(Instructor, null=True,on_delete=models.CASCADE,verbose_name='导员工号')
    collegeid = models.ForeignKey(College, null=True,on_delete=models.CASCADE,verbose_name='专业名')
    def __str__(self):
        return self.name

class Building(models.Model):
    class Meta:
        verbose_name_plural = "公寓"
    name = models.CharField(max_length=20,primary_key=True,verbose_name='公寓名')
    amount = models.IntegerField(default=0, null=True,verbose_name='寝室数')
    floor_num = models.IntegerField(null=True,verbose_name='楼层数')
    start_time = models.DateField(null=True,verbose_name='启用时间')
    def __str__(self):
        return self.name

class Room(models.Model):
    class Meta:
        verbose_name_plural = "寝室"
    name = models.CharField(max_length=20,primary_key=True,verbose_name='寝室名')
    room_type = models.CharField(max_length=20, null=True,verbose_name='寝室类型')
    capacity = models.IntegerField(default=0, null=True,verbose_name='寝室容量')
    buildingid = models.ForeignKey(Building,on_delete=models.CASCADE,verbose_name='所属公寓')
    cost = models.IntegerField(null=True,verbose_name='住宿费用')
    contact = models.CharField(max_length=20,null=True,verbose_name='电话')
    def __str__(self):
        return self.name

class Student(models.Model):
    class Meta:
        verbose_name_plural = "学生"
    sno = models.ForeignKey(Owner,on_delete=models.CASCADE,primary_key=True,verbose_name='学号')
    name = models.CharField(max_length=20,verbose_name='姓名')
    sex = models.NullBooleanField(null=True,verbose_name='性别')
    classid = models.ForeignKey(Class, null=True,on_delete=models.CASCADE,verbose_name='班级')
    roomid = models.ForeignKey(Room, null=True,on_delete=models.CASCADE,verbose_name='房间名')
    contact = models.CharField(max_length=200, null=True,verbose_name='联系方式')
    nation = models.CharField(max_length=20,null=True,verbose_name='民族')
    buildingid = models.ForeignKey(Building, on_delete=models.CASCADE,null=True,verbose_name='公寓号')
    collegeid = models.ForeignKey(College,on_delete=models.CASCADE,null=True,verbose_name='专业')
    def __str__(self):
        return self.name


class Secretary(models.Model):
    class Meta:
        verbose_name_plural = "书记"
    user = models.ForeignKey(Owner,primary_key=True,on_delete=models.CASCADE,verbose_name='工号')
    name = models.CharField(max_length=20,verbose_name='姓名')
    contact = models.CharField(max_length=200, null=True,verbose_name='联系方式')
    collegeid = models.ForeignKey(College,on_delete=models.CASCADE,verbose_name='管辖专业')
    def __str__(self):
        return self.name


class Housemaster(models.Model):
    class Meta:
        verbose_name_plural = "舍管"
    user = models.ForeignKey(Owner,primary_key=True,on_delete=models.CASCADE,verbose_name='工号')
    name = models.CharField(max_length=20,verbose_name='姓名')
    contact = models.CharField(max_length=200, null=True,verbose_name='联系方式')
    buildingid = models.ForeignKey(Building, null=True,on_delete=models.CASCADE,verbose_name='管辖公寓')
    def __str__(self):
        return self.name

class Mark(models.Model):
    class Meta:
        verbose_name_plural = "评分"
    roomid = models.ForeignKey(Room,primary_key=True,on_delete=models.CASCADE,verbose_name='寝室号')
    dt = models.DateTimeField(verbose_name='评分时间')
    score = models.FloatField(verbose_name='分数')
    housemasterid = models.ForeignKey(Housemaster,on_delete=models.CASCADE,verbose_name='评分人工号')
    remark = models.TextField(null=True,verbose_name='评分依据')


class Fee(models.Model):
    class Meta:
        verbose_name_plural = "电费余额"
    roomid = models.ForeignKey(Room, primary_key=True,on_delete=models.CASCADE,verbose_name='寝室号')
    remain = models.FloatField(verbose_name='剩余电量')

class FeeRecord(models.Model):
    class Meta:
        verbose_name_plural = "电费记录"
    roomid = models.ForeignKey(Room,primary_key=True,on_delete=models.CASCADE,verbose_name='寝室号')
    dt = models.DateTimeField(verbose_name='充电时间')
    amount = models.FloatField(verbose_name='充电量')


class Maintenance(models.Model):
    class Meta:
        verbose_name_plural = "维修人员"
    user = models.ForeignKey(Owner,primary_key=True,on_delete=models.CASCADE,verbose_name='工号')
    name = models.CharField(max_length=20,verbose_name='姓名')
    contact = models.CharField(max_length=200, null=True,verbose_name='联系方式')
    def __str__(self):
        return self.name

class Repair(models.Model):
    class Meta:
        verbose_name_plural = "维修记录"
    item = models.CharField(max_length=20,primary_key=True,verbose_name='维修物件')
    roomid = models.ForeignKey(Room,on_delete=models.CASCADE,verbose_name='寝室号')
    book_dt = models.DateTimeField(verbose_name='记录时间')
    reason = models.TextField(null=True,verbose_name='维修原因')
    fix_dt = models.DateTimeField(null=True,verbose_name='修理时间')
    maintenanceid = models.ForeignKey(Maintenance, null=True,on_delete=models.CASCADE,verbose_name='维修人员工号')
    remark = models.TextField(null=True,verbose_name='维修结果')
    def __str__(self):
        return self.item

class QuitApply(models.Model):
    class Meta:
        verbose_name_plural = "退宿申请"
    sno = models.ForeignKey(Student,primary_key=True,on_delete=models.CASCADE,verbose_name='申请人学号')
    roomid = models.ForeignKey(Room,on_delete=models.CASCADE,verbose_name='申请人寝室号')
    dt = models.DateTimeField(verbose_name='退宿申请时间')
    reason = models.TextField(verbose_name='退宿原因')
    housemaster_check = models.NullBooleanField(null=True,verbose_name='舍管审核')
    instructor_check = models.NullBooleanField(null=True,verbose_name='导员审核')
    secretary_check = models.NullBooleanField(null=True,verbose_name='书记审核')


class EnterApply(models.Model):
    class Meta:
        verbose_name_plural = "住宿申请"
    sno = models.ForeignKey(Student,primary_key=True,on_delete=models.CASCADE,verbose_name='申请人学号')
    roomid = models.ForeignKey(Room,on_delete=models.CASCADE,verbose_name='申请宿舍号')
    dt = models.DateTimeField(verbose_name='住宿申请时间')
    housemaster_check = models.NullBooleanField(null=True,verbose_name='舍管审核')
    instructor_check = models.NullBooleanField(null=True,verbose_name='导员审核')
    secretary_check = models.NullBooleanField(null=True,verbose_name='书记审核')

class LiveRecord(models.Model):
    class Meta:
        verbose_name_plural = "住宿记录"
    sno = models.ForeignKey(Student,primary_key=True,on_delete=models.CASCADE,verbose_name='学号')
    roomid = models.ForeignKey(Room,on_delete=models.CASCADE,verbose_name='寝室号')
    enter_time = models.DateTimeField(verbose_name='入住时间')
    quit_time = models.DateTimeField(null=True,verbose_name='退宿时间')


class Visitor(models.Model):
    class Meta:
        verbose_name_plural = "来访记录"
    name = models.CharField(max_length=20,primary_key=True,verbose_name='姓名')
    sex = models.BooleanField(verbose_name='性别')
    document_type = models.CharField(max_length=20, null=True,verbose_name='证件类型')
    documentno = models.CharField(max_length=20, null=True,verbose_name='证件号')
    contact = models.CharField(max_length=200, null=True,verbose_name='联系方式')
    dt = models.DateTimeField(verbose_name='来访时间')
    housemasterid = models.ForeignKey(Housemaster,on_delete=models.CASCADE,verbose_name='舍管工号')
    def __str__(self):
        return self.name




