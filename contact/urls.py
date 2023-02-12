
from django.urls import path,include
from . import views



app_name='contact'
#views.course_list()
urlpatterns = [
    path('',views.show_contact,name="contact") ,

]


