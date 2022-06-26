from django.contrib import admin
from django.urls import path
from students.views import MyView, AllSubjects, GetStudents

urlpatterns = [
    path("cources/subject/", AllSubjects.as_view()),
    path("cources/subject/<id>/", GetStudents.as_view())
]
