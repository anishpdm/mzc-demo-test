from django.urls import path,include
from .views import PostCreateView
from . import views

urlpatterns = [
    path('', views.myHomePage,name='homepage'),
    path('post/', PostCreateView.as_view(template_name='login.html'),name='Newpost'),
]
