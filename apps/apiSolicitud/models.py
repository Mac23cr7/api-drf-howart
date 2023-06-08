from django.db import models

# Create your models here.
class School(models.Model):
    houseId = models.AutoField(primary_key=True)
    houseName = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        verbose_name = 'School'
        verbose_name_plural = 'Schools'

    def __str__(self):
        return self.houseName

class Request(models.Model):
    requestId = models.AutoField(primary_key=True)
    studentName = models.CharField(max_length=100, null=False, blank=False)
    studentSurname = models.CharField(max_length=100, null=False, blank=False)
    identification = models.CharField(max_length=100, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    idSchool = models.ForeignKey(School, on_delete = models.CASCADE, null = False, blank = False)

    class Meta:
        verbose_name = 'Request'
        verbose_name_plural = 'Requests'

    def __str__(self):
        return self.studentName
