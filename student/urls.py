from django.urls import path

from . import views

urlpatterns = [
    path('attendance/', views.attendancefun, name='attendancefun'),
path('marks/', views.marks, name='marks'),
#path('assingment/', views.assingment, name='assingment'),
]
