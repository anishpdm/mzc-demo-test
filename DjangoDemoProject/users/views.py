from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  #Save To Db
            username=form.cleaned_data.get('username') 
            messages.success(request,f'Account created for the {username}')
            return redirect('login')
        else:
            return redirect('register')    
            # return render(request,'register.html',context)


    else:    
        form = UserCreationForm()
    # ///
    
        context={'form':form}
        return render(request,'register.html',context)


