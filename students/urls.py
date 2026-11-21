from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("greet/",views.greet_student,name="greet"),
    path("age/<int:age>/",views.student_age,name="age"),
    path("calculate/", views.calculate_age, name="calculate"),
]