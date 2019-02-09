from django.http import HttpResponse
from django.shortcuts import render
from challenges.models import CommunityChallenge

def challenges(request):
    num_challenge_posts = CommunityChallenge.objects.all().count()

    context = {
        'num_challenge_posts': num_challenge_posts,
    }


    return render(request, 'challenges.html', context=context)