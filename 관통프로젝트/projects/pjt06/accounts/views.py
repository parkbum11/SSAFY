from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login , logout as auth_logout
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth import get_user_model
# Create your views here.


@require_http_methods(['GET','POST'])
def signup(request):
    
    if request.user.is_authenticated:
        return redirect('community:review_list')
        
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user= form.save()
            auth_login(request,user)
            return redirect('community:review_list')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)


@require_http_methods(['GET','POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('community:review_list')

    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'community:review_list')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html',context)


@require_POST
def logout(request):
    auth_logout(request)
    return redirect('community:review_list')

def profile(request,username):
    person = get_object_or_404(get_user_model(),username = username)
    context = {
        'person':person,
    }
    return render(request, 'accounts/profile.html',context)

@require_POST
def follow(request,user_pk):
    person = get_object_or_404(get_user_model(),pk=user_pk)
    user = request.user
    if person != user:
        if person.followers.filter(pk=user.pk).exists():
            person.followers.remove(request.user.pk)
        else:
            person.followers.add(request.user.pk)
    return redirect('accounts:profile',person.username)

