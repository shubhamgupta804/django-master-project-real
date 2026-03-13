from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# add stduent view function
@csrf_exempt
def add_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        student = Student(name=name, email=email, age=age)
        student.save()
        return HttpResponse('Student added successfully')
    return HttpResponse('Invalid request method')

# create a view for update student
@csrf_exempt
def update_student(request, id):
    if request.method == 'POST':
        student = Student.objects.get(id=id)
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.age = request.POST['age']
        student.save()
        return HttpResponse('Student updated successfully')
    return HttpResponse('Invalid request method')

# create a view for delete student
@csrf_exempt
def delete_student(request, id):
    if request.method == 'POST':
        student = Student.objects.get(id=id)
        student.delete()
        return HttpResponse('Student deleted successfully')
    return HttpResponse('Invalid request method')

# create a view for list student in repsonse for postman
@csrf_exempt
def list_student(request):
    students = Student.objects.all()
    student_list = []
    for student in students:
        student_list.append({'name': student.name, 'email': student.email, 'age': student.age})
    return HttpResponse(student_list)


# import base64
# from django.http import JsonResponse
# from django.core.files.base import ContentFile
# from django.shortcuts import render
# from .models import AutoCapture

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import AutoCapture

def camera_page(request):
    return render(request, "camera.html")


@csrf_exempt

def save_data(request):
    print("Data received")

    if request.method == "POST":

        image = request.FILES.get("image")
        lat = request.POST.get("lat")
        lon = request.POST.get("lon")
        alt = request.POST.get("alt")

        if not image:
            return JsonResponse({"error": "No image received"})

        # convert values safely
        lat = float(lat) if lat not in [None, ""] else None
        lon = float(lon) if lon not in [None, ""] else None
        alt = float(alt) if alt not in [None, ""] else None

        AutoCapture.objects.create(
            image=image,
            latitude=lat,
            longitude=lon,
            altitude=alt
        )

        return JsonResponse({"status": "saved"})