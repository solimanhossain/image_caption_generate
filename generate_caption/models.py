from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images', verbose_name='Image')

    # @property
    def __str__(self):
        return self.title
