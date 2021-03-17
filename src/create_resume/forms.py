from django import forms
from django.shortcuts import render

from create_resume.models import *


class ResumeForm(forms.Form):
    first_name = Worker.objects.first_name()

