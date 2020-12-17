# -*- coding: utf-8 -*-
__author__ = 'ffuentes'

from django.contrib import admin
from .models import Stream, TokenType, Token

# Register your models here.

admin.site.register(Stream)
admin.site.register(TokenType)
admin.site.register(Token)
