from django.db import models

class CommunityChallenge(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=200)
    #difficulty level
    #timestamp
    #set of mentee responses/solutions
    # author = ForeignKey(User)??

    def __str__(self):
        return self.title
    


# Class Comments(models.Model){


# }