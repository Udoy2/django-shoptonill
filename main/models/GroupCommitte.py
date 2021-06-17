from django.db import models

# Create your models here.


class GroupCommitte(models.Model):
    full_name = models.CharField(max_length=60)
    designation = models.CharField(max_length=60)
    profile_pic = models.ImageField(upload_to='committe_profile_pic',
                                    null=True,
                                    blank=True)

    def __str__(self):
        return self.full_name


class Shobhapoti(models.Model):
    full_name = models.CharField(max_length=60)
    quotation = models.CharField(max_length=500)
    profile_pic = models.ImageField(upload_to='shobhapoti',
                                    null=True,
                                    blank=True)

    def __str__(self):
        return self.full_name
