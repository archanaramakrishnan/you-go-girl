from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=200)
    # author = ForeignKey(User)

    def __str__():
        return self.title
    


# Class Comments(models.Model){


# }