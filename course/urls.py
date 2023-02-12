
from django.urls import path,include
from . import views


from django.conf import settings
from django.conf.urls.static import static

app_name='course'
#views.course_list()
urlpatterns = [
    path('',views.course_list,name='course_list') ,
    path('<pk>',views.course_detail,name="course_detail"),
]

urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

