from django.shortcuts import render
from .models import Student


# Create your views here.
def home(request):
    return render(request, 'index.html')


def student(request):
    stude = Student.objects.all()
    return render(request, 'student.html', {"pupil": stude})
