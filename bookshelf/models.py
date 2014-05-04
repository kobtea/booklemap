# coding: utf-8
from django.db import models


class Status(models.Model):
    STATUS = (
        ('have', 'もってる！'),
        ('wish', 'ほしい！'),
    )
    # user = models.ForeignKey('social_auth.UserSocialAuth')
    # FIXME: use foreign key
    user = models.IntegerField()
    asin = models.CharField(max_length=20)
    status = models.CharField(max_length=4, choices=STATUS)
