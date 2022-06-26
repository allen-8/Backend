from django.contrib import admin
from django.urls import path, include
from students.views import MyView, AllSubjects

urlpatterns = [
    path('admin/', admin.site.urls),
    path("view/", MyView.as_view()),
    path("students/", include("students.urls"))
]
