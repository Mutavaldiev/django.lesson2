from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('auth/', auth_page, name='auth'),
    path('courses/', courses_page, name='courses'),
    path('course-detail/', course_detail_page, name='course_detail'),
    path('profile/', profile_page, name='profile'),
]