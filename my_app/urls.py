from django.urls import path 
from my_app.views import *

urlpatterns = [
    path('student_view',student_view,name='student_view'),
    path('subject_view',subject_view,name='subject_view'),
    path('subject_detail/<int:id>',subject_detail,name='subject_detail'),
]