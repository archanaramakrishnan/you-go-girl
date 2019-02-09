from django.urls import path

from . import views

urlpatterns = [
    # Behavior defined in yougogirl/blog/views.py as blog()
    #URL to access this page: http://127.0.0.1:8000/blog/
    path('', views.challenges, name='challenges'),
]