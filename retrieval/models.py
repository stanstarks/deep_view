from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Datum:
    def __init__(self, name, label, predict, rawlabel):
        self.name = name
        self.label = label
        self.predict = predict
        self.rawlabel = rawlabel
