from django.shortcuts import render
from .models import Worker, Hard_skills, Soft_skills, Photo_worker, Projects


def home(request):
    worker = Worker.objects.all()
    hs = Hard_skills.objects.all()
    ss = Soft_skills.objects.all()
    photo = Photo_worker.objects.all()
    projects = Projects.objects.all()
    data = {'worker': worker, 'hs': hs, 'ss': ss, 'photo': photo, 'projects': projects}
    return render(request, 'base.html', data)
