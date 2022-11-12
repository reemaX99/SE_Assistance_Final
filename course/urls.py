
from django.urls import path,include
from . import views
from course.views import course_list ,course_detail


#views.course_list()
urlpatterns = [
    path('',course_list) ,
    path('<pk>',course_detail),
]

