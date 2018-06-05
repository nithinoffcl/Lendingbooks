from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .forms import SignupForm,LoginForm
from .models import User
from django.shortcuts import get_object_or_404

urls1 = {
1 : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSq7ot1SZ3ShFHl4hvnPrhf-dXTxx35frPANTzSzHfrPQVIZspt",
2 :"https://image.freepik.com/free-vector/book-cover-template-design_1201-30.jpg",
3 : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTUQpbW1biwSNk7y5lDEXzKzqklEUxi2OJSrUv5Ty0YnwTfg93S7w"
}
urls2 = {
4 : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwXlXkb8VUo8EZQ0xDclZUODDJmpiHOS-GBdceSRYyzfmem5SYLA",
5 : "http://1.bp.blogspot.com/-Wca-FWqIqV4/UkzMVvHPw-I/AAAAAAAAARw/D2TaC-X5fVw/s1600/MathSkillsWorkbook-CoverFinal.jpg",
6 : "http://1.media.collegehumor.cvcdn.com/c/8/collegehumor.d92dfb4c8dd29dc3d678290811a920b8.jpg"
}

urls = {

1 : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSq7ot1SZ3ShFHl4hvnPrhf-dXTxx35frPANTzSzHfrPQVIZspt",
2 :"https://image.freepik.com/free-vector/book-cover-template-design_1201-30.jpg",
3 : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTUQpbW1biwSNk7y5lDEXzKzqklEUxi2OJSrUv5Ty0YnwTfg93S7w",
4 : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwXlXkb8VUo8EZQ0xDclZUODDJmpiHOS-GBdceSRYyzfmem5SYLA",
5 : "http://1.bp.blogspot.com/-Wca-FWqIqV4/UkzMVvHPw-I/AAAAAAAAARw/D2TaC-X5fVw/s1600/MathSkillsWorkbook-CoverFinal.jpg",
6 : "http://1.media.collegehumor.cvcdn.com/c/8/collegehumor.d92dfb4c8dd29dc3d678290811a920b8.jpg",

}


def temp(request,):
    q = request.session['query']
    user = User.objects.get(email = q)
    return render(request,'books/temp.html',{'user':user,'data1':urls1,'data2':urls2})

def requestconfirmation(request,value):
    p = request.session['query']
    url = urls[value]
    user = User.objects.get(email = p)
    return render(request,'books/requestconfirmation.html',{'user':user,'id':value,'url': url})


def signup(request):
    if request.method == 'POST':
        signup_form = SignupForm(request.POST)

        if signup_form.is_valid():
            signup_form.save()
            signup_form = SignupForm()

    else:
        signup_form = SignupForm()

    return render(request,'books/signup.html',{'form':signup_form})

def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            query = login_form.cleaned_data['email']
            request.session['query'] = query
            login_form.save()
            login_form = LoginForm()
            return HttpResponseRedirect('/temp')

    else:
        login_form = LoginForm()

    return render(request,'books/login.html',{'form':login_form})
