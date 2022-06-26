from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from students.models import Student, Subject


class GetStudents(View):

    def get(self, request, id):
        students = []
        try:
            subj = Subject.objects.get(id=id)
            groups = subj.groups.all()
            for g in groups:
                st = g.students.all()
                for s in st:
                    students.append({"name": s.name})
        except Subject.DoesNotExist:
            students.append({"Error!": "Subject with such ID does not exists!"})
        return JsonResponse({"data": students})


class AllSubjects(View):

    def get(self, request):
        subj = Subject.objects.all()
        subjs = []
        for s in subj:
            subjs.append({"name": s.name})
        return JsonResponse({"data": subjs})


class MyView(View):

    def get(self, request):
        name = request.GET.get("name", "0")
        students = Student.objects.all()
        if name:
            students = students.filter(name=name)
        students_data = []
        for student in students:
            students_data.append({"name": student.name})
        return JsonResponse({"data": students_data})

    def post(self, request):
        name = request.data.get("name", "0")



# Create your views here.
