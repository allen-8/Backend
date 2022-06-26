from django.db import models


class Subject(models.Model):
    name = models.CharField(verbose_name="Name", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"


class Group(models.Model):
    name = models.CharField(verbose_name="Name", max_length=100)
    amountStudents = models.IntegerField(verbose_name="Amount of students", blank=True, null=True)
    subject = models.ForeignKey(Subject, verbose_name="Subject", on_delete=models.SET_NULL, null=True,
                                related_name="groups")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"


class Student(models.Model):
    name = models.CharField(verbose_name="Name", max_length=100)
    group = models.ForeignKey(Group, verbose_name="Group", on_delete=models.SET_NULL, null=True,
                              related_name="students")
    birthday = models.DateField(verbose_name="Birthday", default="2000-1-1")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
