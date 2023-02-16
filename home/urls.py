
from django.urls import path,include
from . import views


from django.conf import settings
from django.conf.urls.static import static

app_name='home'
#views.course_list()
urlpatterns = [
    path('',views.show_home,name='home') ,

]



