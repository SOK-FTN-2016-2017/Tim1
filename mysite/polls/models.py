# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.utils.encoding import force_bytes

def __str__(self):
    return force_bytes(self.name)

def __unicode__(self):
    return self.name