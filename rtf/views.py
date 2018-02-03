# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.template import loader
from logging.handlers import SMTPHandler
from django import forms
from django.core.files.storage import FileSystemStorage
from rtf.models import *
from django.conf import settings
from datetime import *
import logging


# Create your views here.

def index(request):
    return HttpResponse("OK")
