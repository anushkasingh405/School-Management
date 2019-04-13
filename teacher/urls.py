from django.urls import path

from . import views

urlpatterns = [
    path('attendance/', views.attendancefunc, name='attendance'),
path('marks/', views.marks, name='marks'),
path('exam/', views.examfunc, name='exam'),
]
