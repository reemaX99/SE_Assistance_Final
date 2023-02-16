from django.shortcuts import render
from contact.models import contact
from course.models import course

# Create your views here.


def show_home(request):
    contact_list = contact.objects.all()
    course_list = course.objects.all()
    context = {'contact':  contact_list, 'course': course_list}
    return render(request,'home/index.html',context)