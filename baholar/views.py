from django.shortcuts import render
from .models import Grade,Student,Subject


#home page view
def home_page(request):
    students=Grade.objects.all()
    context={
        "students":students
    }
    return render(request,"home.html",context)



