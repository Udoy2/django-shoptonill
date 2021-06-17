from django.db import models
from django.db.models.fields.files import ImageField


class Gallery(models.Model):
    gallery_pic = ImageField(upload_to='gallery', null=True, blank=True)

    def __str__(self):
        return f'gallery_pic: {self.pk}'
