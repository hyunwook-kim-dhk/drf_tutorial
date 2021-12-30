from django.contrib.auth.models import User
from django.db import models


class Schedule(models.Model):
    TAG_CHOICES = (
        ('DRIVE', u'드라이브'),
        ('MEAL', u'식사'),
    )

    user = models.ForeignKey(User, null=False, on_delete=models.DO_NOTHING)
    start_datetime = models.DateTimeField(null=False)
    end_datatime = models.DateTimeField(null=False)
    summary = models.CharField(max_length=80, null=False)
    description = models.TextField(null=True)
    tags = models.CharField(max_length=5, null=True, choices=TAG_CHOICES)
