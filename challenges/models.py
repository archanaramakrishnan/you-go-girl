from django.db import models
from django.utils import timezone

class CommunityChallenge(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=2000)
    published_date = models.DateTimeField(blank=True, null=True)

    #difficulty level
    #set of mentee responses/solutions
    # author = ForeignKey(User)??

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    


# Class Comments(models.Model){


# }