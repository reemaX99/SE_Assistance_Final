from django.shortcuts import render
from .models import course
from django.http import HttpResponse

# Create your views here.
def course_list(request):
    course_list = course.objects.all()
    context = {'course': course_list}  # here the name goes to the templete
    return render(request, 'course/course_list.html', context )


def course_detail(request, pk):
    course_detail= course.objects.get(id=pk)
    context = {'course': course_detail}  # here the name goes to the templete
    return render(request, 'course/course_detail.html', context)
