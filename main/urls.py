
from django.urls import path
from . import views

urlpatterns = [
    path('insta_day', views.insta_day.as_view()),
    path('get_replace_data', views.get_replace_data.as_view()),
    path('insta_msg', views.insta_msg.as_view()),
    path('', views.insta_time_counter.as_view()),
    path('error', views.instabot_error.as_view()),
]
