from django.shortcuts import render
from . import models as quiz_models

def dashboard(request):

    categorys = quiz_models.Category.objects.all()

    context = {
        'categorys': categorys
    }

    return render(request, 'quiz/dashboard.html', context)