from django.http import HttpResponse
from django.shortcuts import render
from challenges.models import CommunityChallenge

def challenges(request):
    num_challenge_posts = CommunityChallenge.objects.all().count()
    posts = CommunityChallenge.objects.order_by('-published_date')

    context = {
        'num_challenge_posts': num_challenge_posts,
        'challenges': posts,
    }


    return render(request, 'challenges.html', context=context)