from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def registration(request):
    d={'EUFO':UserForm(),'EPFO': ProfileForm()}
    if request.method=='POST' and request.FILES:
        EUFO=UserForm(request.POST)
        EPFO=ProfileForm(request.POST,request.FILES)
        if EUFO.is_valid()  and EPFO.is_valid():
            MUFDO=EUFO.save(commit=False)
            pw=EUFO.cleaned_data['password']
            MUFDO.set_password(pw)
            MUFDO.save()
            MPFDO=EPFO.save(commit=False)
            MPFDO.username=MUFDO
            MPFDO.save()
            return HttpResponse('register successfully')
        else:
            return HttpResponse('invalid data')
    return render(request,'registration.html',d)
