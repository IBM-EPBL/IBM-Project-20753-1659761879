from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from accounts.forms import ProfileForm
from accounts.models import Profile
import requests
import json
from .models import JobApplied


CustomUser = get_user_model()
@login_required(login_url='account_login')
def home(request):
    
    job_list = []
    url = requests.get('https://arbeitnow.com/api/job-board-api')
    response = url.text
    json_data = json.loads(response)
    for i in range(0,40):

        a = json_data["data"][i]["company_name"]
        b = json_data["data"][i]["title"]
        c = json_data["data"][i]["location"]
        job_list.append([a,b,c])
       
    id =request.user.id
    current_user = get_object_or_404(CustomUser, id=id)
    profile = Profile.objects.get(user=current_user)
    if request.method == "POST":
        # form = JobApplied(request.POST)
        data_submitted = request.POST.dict()
        object = JobApplied(user=profile,title=data_submitted["title"], location=data_submitted["location"], company_name= data_submitted["company_name"])
        object.save()
        print(data_submitted)

    

    context = {
        "job_list":job_list,

  
     
    }
    return render(request,'home.html',context)


@login_required(login_url='account_login')
def profile(request, id):
    current_user = get_object_or_404(CustomUser, id=id)
    profile = Profile.objects.get(user=current_user)
    job_applied = JobApplied.objects.filter(user=profile).all()
    if current_user != request.user:
        return HttpResponseBadRequest('error 404')
    else:
        
        form = ProfileForm(instance=profile)
        if request.method == 'POST':
            form = ProfileForm(request.POST, instance=profile)
            if form.is_valid():
                
                save_form = form.save(commit=False)
                save_form.user = request.user
                form.save()
                print("es")
                return redirect('profile', id=str(request.user.id))
    context = {
        'form':form,
        'job_applied': job_applied
    }
    return render(request, 'profile.html', context)





