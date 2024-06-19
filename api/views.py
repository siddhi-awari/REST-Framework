from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
#for single student
def student_detail(request, pk):
    stu = Student.objects.get(id=pk)
    '''print(stu)
    Student object (3)'''
    serializer = StudentSerializer(stu)
    '''print(serializer)
    StudentSerializer(<Student: Student object (3)>):
    id = IntegerField()
    name = CharField(max_length=100)
    roll = IntegerField()
    city = CharField(max_length=100)
    print(serializer.data)
    {'id': 3, 'name': 'Siddhi', 'roll': 1, 'city': 'Mumbai'}'''
    #json_data = JSONRenderer().render(serializer.data)
    '''print(json_data)
    {"id":3,"name":"Siddhi","roll":1,"city":"Mumbai"}'''
    #return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)

'''class StudentView(APIView):
    def get(self,request):
        allStudents = Student.objects.all().values()
        return Response({"Message":"List of Students","Student list":allStudents})

    def post(self,request):
        Student.objects.create(id = request.data["id"],
                                name = request.data["name"],
                                roll = request.data["roll"],
                                city = request.data["city"]        
                                )
        Students = Student.objects.all().values()
        return Response({"Message":"New Student","Student":Students})'''

def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many = True)
    #json_data = JSONRenderer().render(serializer.data)

    #return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data, safe = False)
