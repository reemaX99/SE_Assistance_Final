from django.shortcuts import render
from .models import course
from django.http import HttpResponse
from django.core.paginator import Paginator
from .filters import CourseFilter

# Create your views here.
def course_list(request):
    course_list = course.objects.all()
    ## filters
    myfilter = CourseFilter(request.GET, queryset=course_list)
    course_list = myfilter.qs

    paginator = Paginator(course_list, 3) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'course': page_obj, 'myfilter' : myfilter}  # here the name goes to the templete
    return render(request, 'course/course_list.html', context )


def course_detail(request, pk):
    course_detail= course.objects.get(id=pk)
    context = {'course': course_detail}  # here the name goes to the templete
    return render(request, 'course/course_detail.html', context)

