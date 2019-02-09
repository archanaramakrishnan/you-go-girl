from django.http import HttpResponse
from django.shortcuts import render
from users.models import Profile
	
def profile(request):
    username=None

    # if request.user.is_authenticated():
    #     username = request.user.username

    if request.user.profile.role==2:
        mntr_status = True

    context = {
        'mentor_status': mntr_status,
        'fname': request.user.first_name,
        'lname': request.user.last_name,
        'email': request.user.email, 
        'location': request.user.profile.location,
        'bio': request.user.profile.bio,        
    }

    return render(request, 'update_profile.html', context=context)