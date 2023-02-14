
from django.urls import path,include
from . import views
from chatbots.views import predict

from django.conf import settings
from django.conf.urls.static import static

app_name='chatbots'
#views.course_list()
urlpatterns = [
    path('/predict',predict)
]


