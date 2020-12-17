# -*- coding: utf-8 -*-
__author__ = 'ffuentes'

import os


class Database:
    NAME = os.getenv('POSTGRES_DB')
    USER = os.getenv('POSTGRES_USER')
    PASSWORD = os.getenv('POSTGRES_PASSWORD')
    HOST = os.getenv('DATABASE_HOST')
    PORT = os.getenv('DATABASE_PORT')


class Secrets:
    SECRET_KEY = "ChangeThisKey"


class AppSettings:
    SERVER_TYPE = os.getenv('SERVER_TYPE', 'dev')
    HAS_USER_REGISTRATION = os.getenv('HAS_USER_REGISTRATION', False)
    HAS_AD_ENGINE = os.getenv('HAS_AD_ENGINE', False)
