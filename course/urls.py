
from django.urls import path,include
from . import views
from course.views import course_list ,course_detail

from django.conf import settings
from django.conf.urls.static import static

app_name='course'
#views.course_list()
urlpatterns = [
    path('',course_list) ,
    path('<pk>',course_detail,name="course_detail"),
]

urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

