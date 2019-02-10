from django.urls import path
from users import views
from django.conf.urls import url, include

urlpatterns = [
    # Behavior defined in yougogirl/blog/views.py as blog()
    #URL to access this page: http://127.0.0.1:8000/profile/
    path('profile', views.profile, name='profile'),
    path('mentor_list', views.mentor_list, name='mentor_list'),

    url(r'^$', views.signup, name='signup'),

]