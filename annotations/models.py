from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class ImageLabel(models.Model):
    image = models.CharField(max_length=100, db_index=True)
    label = models.CharField(max_length=40)

    def __str__(self):
        return self.image + ':' + self.label

# All modifications are pending. Once applied to image label table, records will be deleted.
class Modification(models.Model):
    ip = models.CharField(max_length=20)
    date = models.DateTimeField('date modified', db_index=True)
    from_label = models.CharField(max_length=40)
    to_label = models.CharField(max_length=40)
    image = models.CharField(max_length=100, db_index=True)

    def was_modified_within(delta):
        return self.data > timezone.now() - delta
