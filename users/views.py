from django.http import HttpResponse
from django.shortcuts import render, redirect
from users.models import Profile
from users.forms import SignUpForm
from django.contrib.auth import authenticate, login

def profile(request):
    username=None

    if request.user.profile.role==2:
        mntr_status = True

    mentor_info = {
        'hrs_available': request.user.profile.hrs_per_week_available,
        'university': request.user.profile.university,
        'company': request.user.profile.company,
    }

    mentee_info = {
        'skill_level': request.user.profile.skill_level,
        'grade': request.user.profile.grade_in_school,
    }

    context = {
        'mentor_status': mntr_status,
        'fname': request.user.first_name,
        'lname': request.user.last_name,
        'email': request.user.email, 
        'location': request.user.profile.location,
        'bio': request.user.profile.bio,
        'spoken_language': request.user.profile.spoken_language,
        'preferred_programming_language': request.user.profile.preferred_programming_language,
        'mentor_info': mentor_info,
        'mentee_info': mentee_info,
    }

    return render(request, 'update_profile.html', context=context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            
            user.profile.birthdate = form.cleaned_data.get('birthdate')
            user.profile.location = form.cleaned_data.get('location')
            user.profile.spoken_language = form.cleaned_data.get('spoken_language')
            user.profile.preferred_programming_language = form.cleaned_data.get('preferred_programming_language')
            user.profile.bio = form.cleaned_data.get('bio')
            if form.cleaned_data.get('sign_up_as_mentor'):
                # Mentor role
                user.profile.role = 2
            else: 
                # Mentee role
                user.profile.role = 1
            user.profile.hrs_per_week_available = form.cleaned_data.get('hrs_per_week_available')
            user.profile.university = form.cleaned_data.get('university')
            user.profile.company = form.cleaned_data.get('company')
            
            # Finally, save that data we collected
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('challenges')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})