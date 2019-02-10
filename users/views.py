from django.http import HttpResponse
from django.shortcuts import render
from users.models import Profile
	
def profile(request):
    username=None

    # if request.user.is_authenticated():
    #     username = request.user.username

    if request.user.profile.role==2:
        mntr_status = True

    mentor_info = {
        'hrs_available': request.user.profile.hrs_per_week_available,
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
        'mentor_info': mentor_info,
        'mentee_info': mentee_info,
    }

    return render(request, 'update_profile.html', context=context)