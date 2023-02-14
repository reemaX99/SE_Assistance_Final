
from django.urls import path,include
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name='learn'
#views.course_list()
urlpatterns = [
    path('',views.post_learn,name="learn") ,
    path('blog',views.blog, name="blog"),
    path('blog/<pk>', views.blog_detail, name="blog_detail"),


]

urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

