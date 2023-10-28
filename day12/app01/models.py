from django.db import models

# Create your models here.
from django.db import models


# Create your models here.


class Student(models.Model):
    student_id = models.AutoField(primary_key=True, verbose_name="学生编号")
    student_name = models.CharField(max_length=8, verbose_name="学生姓名")
    student_gender = models.BooleanField(
        choices=([0, "male"], [1, "female"]), default=0, verbose_name="学生性别")
    student_class = models.ForeignKey(
        to="Classes", verbose_name="所属班级", on_delete=models.CASCADE)  # 一个班级多个学生

    def __str__(self):
        return self.student_name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Student'
        verbose_name_plural = 'Students'


class Classes(models.Model):
    class_id = models.AutoField(primary_key=True, verbose_name="班级编号")
    class_name = models.CharField(max_length=8, verbose_name="班级名称")
    class_teacher = models.OneToOneField(
        to="Teacher", verbose_name="班主任", on_delete=models.CASCADE)  # 一个班级只有一个班主任

    def __str__(self):
        return self.class_name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Classes'
        verbose_name_plural = 'Classess'


class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True, verbose_name="教师编号")
    teacher_name = models.CharField(max_length=8, verbose_name="教师姓名")
    teacher_class = models.ManyToManyField(
        to="Classes", verbose_name="任教班级")  # 一个班级中可有多个老师，一个老师也可以在多个班级中任教

    def __str__(self):
        return self.teacher_name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

