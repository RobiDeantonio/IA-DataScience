""" User.views"""

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

#exceptions
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User
from users.models import Profile

# Forms
from users.forms import ProfileForm

@login_required
def update_profile(request):

    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            profile.website = data['website']
            profile.biography = data['biography']
            profile.phone_number = data['phone_number']
            profile.picture = data['picture']
            profile.save()
             
            return redirect('update_profile')
    else:
        form = ProfileForm()
    
    return render(request = request, 
    template_name='users/update_profile.html', 
    context={
        'profile':profile, 
        'user':request.user,
        'form' :form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html',{'error': 'Invalid username and password'})
    return render(request,'users/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['password']
        passwd_confirmation = request.POST['pass_confirmation']
        
        if passwd != passwd_confirmation:
            return render(request, 'users/signup.html', {'error':'password does not match'})

        try:
            user = User.objects.create_user(username=username, password=passwd)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error':'username is already in use'})            
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.save()

        return redirect('login')
    return render(request,'users/signup.html')

