from __future__ import unicode_literals

from django.db import models

class ImageLabel(models.Model):
    image = models.CharField(max_length=100)
    label = models.CharField(max_length=40)

    def __str__(self):
        return self.image + ':' + self.label

class Modification(models.Model):
    ip = models.IntegerField()
    date = models.DateTimeField('date modified')
    from_label = models.CharField(max_length=40)
    to_label = models.CharField(max_length=40)
    image = models.ForeignKey(ImageLabel, on_delete=models.CASCADE)

    def was_modified_within(delta):
        return self.data > timezone.now() - delta

