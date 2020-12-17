# -*- coding: utf-8 -*-
__author__ = 'ffuentes'

from django.db import models
from django.contrib.auth.models import User

import uuid

# Create your models here.

class Stream(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    description = models.TextField()
    mountpoint = models.CharField(max_length=128)
    run_ads = models.BooleanField(default=False)
    max_clients = models.IntegerField(default=50)
    # True: no payment required to access False: Payment required
    free_stream = models.BooleanField(default=True)
    # the users can pay more than the access fee
    flexible_fee = models.BooleanField(default=True)
    access_fee = models.DecimalField(default=0.0, decimal_places=2, 
                    max_digits=4)


class TokenType(models.Model):
    type = models.CharField(max_length=32, unique=True)


class Token(models.Model):
    value = models.UUIDField(primary_key=True, 
		default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token_type = models.ForeignKey(TokenType, on_delete=models.CASCADE)
