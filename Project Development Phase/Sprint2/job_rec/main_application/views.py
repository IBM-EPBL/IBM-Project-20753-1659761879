from django.shortcuts import render
from django.contrib.auth import get_user_model


def home(request):
    context = {
        None:None
    }
    return render(request,'home.html',context)
