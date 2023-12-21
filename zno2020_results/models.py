from django.db import models


class Location(models.Model):
    region_name = models.TextField()
    area_name = models.TextField()
    territory_name = models.TextField()
    territory_type = models.TextField()


class Institution(models.Model):
    name = models.TextField(null=True)
    type = models.TextField(null=True)


class Student(models.Model):
    birth_year = models.IntegerField()
    sex = models.CharField(max_length=255)
    type = models.TextField()
    location = models.ForeignKey(Location,
                                 on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution,
                                    on_delete=models.CASCADE)


class StudentResults(models.Model):
    student = models.ForeignKey(Student,
                                on_delete=models.CASCADE)
    status = models.CharField(max_length=255, null=True)
    ukrball100 = models.IntegerField(null=True)
    ukrball12 = models.IntegerField(null=True)
