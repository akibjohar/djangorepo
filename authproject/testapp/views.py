from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home_view(request):
    return render(request,'testapp/home.html')
def logout_view(request):
    return render(request,'testapp/logout.html')
@login_required
def java_exam(request):
    return render(request,'testapp/javaexam.html')
@login_required
def python_exam(request):
    return render(request,'testapp/pythonexam.html')
@login_required
def apti_exam(request):
    return render(request,'testapp/apptiexam.html')

from testapp.forms import SignUpForm
def signup_view(request):
    form=SignUpForm()
    return render(request,'testapp/signup.html',{'form':form})







# Create your views here.
