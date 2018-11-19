from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Tweets

tweets = [
    {
        'posts':'Testing Project',
        'author':'Anish S Nair',
        'postedDate':'30/11/2018'

    },
    {
        'posts':'Testing Project2',
        'author':'Rahul M',
        'postedDate':'30/11/2018' 
    }
]

class PostCreateView(CreateView):
    model = Tweets
    fields=['content','author']

    def form_valid(self, form):
        # form.instance.author = self.request.user
        return redirect('register')
       # return super().form_valid(form)

def myHomePage(request):
    context={'tweets':Tweets.objects.all()}
    return render(request,'home.html',context)
# Create your views here.
