from django.http import HttpResponse
from django.shortcuts import render
from users.models import Profile
	
def profile(request):
    username=None

    # if request.user.is_authenticated():
    #     username = request.user.username

    if request.user.profile.is_mentor:
        mntr_status = True

    context = {
        'mentor_status': mntr_status,
        
    }

    return render(request, 'update_profile.html', context=context)