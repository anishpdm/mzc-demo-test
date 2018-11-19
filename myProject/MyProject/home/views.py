from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Faculties
from django.views.generic import CreateView

# Create your views here.
# Faculties = [
#     {
#         'FacultyName':'Rajesh',
#         'Designation':'Ass. Professor',
#         'EmailId':'r@gmail.com',
#         'Mobile':'9526674440'
#     },
#     {
#         'FacultyName':'Maya',
#         'Designation':'Ass. Professor',
#         'EmailId':'m@gmail.com',
#         'Mobile':'7979797979'
#     },
#     {
#         'FacultyName':'Remya',
#         'Designation':'Professor',
#         'EmailId':'remya@gmail.com',
#         'Mobile':'66668686'
#     },
#     {
#         'FacultyName':'Rahul R',
#         'Designation':'HOD',
#         'EmailId':'rahulr@gmail.com',
#         'Mobile':'878686886'
#     }

# ]

def myhome(request):
    mydict={'Faculties':Faculties.objects.all()}
    
    return render(request,'home.html',mydict)


def about(request):
    return HttpResponse('My about Page')

class FacultyCreateView(CreateView):
    model=Faculties
    fields=['FacultyName','Designation','EmailId','Mobile']
    def form_valid(self,form):
        form.save()
        return redirect('home')

