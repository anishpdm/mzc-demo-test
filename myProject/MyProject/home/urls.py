from django.urls import path
from . import views
from . views import FacultyCreateView

urlpatterns = [
    path('entry/', FacultyCreateView.as_view(template_name='entry.html') ,name='home'),
    path('', views.myhome,name='home'),
    path('about/',views.about,name='about'),
]