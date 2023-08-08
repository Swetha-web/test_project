from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User
from .forms import UserForm
# Create your views here.
def home(request):
    form=UserForm()
    return render(request,'index.html',{'form':form})
def app(request):
    msg="<form>hi</form>"
    return HttpResponse(msg)

def usersave(request):

    form=UserForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect('list_users')

def list_user(request):
    
    data = User.objects.all()

    return render(request,'first.html', {'users': data}) 