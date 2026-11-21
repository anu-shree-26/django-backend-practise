from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Student Management")

def greet_student(request):
    return HttpResponse("Hello Student!")

def student_age(request,age):
    return HttpResponse(f"Student Age: {age}")

def calculate_age(request):
    age = request.GET.get("age", "18")
    age = int(age)

    return HttpResponse(f"Age after 5 years: {age + 5}")