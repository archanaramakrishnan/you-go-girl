from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    MENTEE = 1
    MENTOR = 2
    ROLE_CHOICES = (
        (MENTEE, 'Mentee'),
        (MENTOR, 'Mentor'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    spoken_language = models.CharField(max_length=50, blank=True)
    preferred_programming_language = models.CharField(max_length=50, blank=True)

    # Mentor Attributes
    hrs_per_week_available = models.IntegerField(default=1)
    university = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)

    # Mentee Attributes
    NEVER_CODED_BEFORE = 1
    BEGINNER = 2
    INTERMEDIATE = 3
    ADVANCED = 4
    EXPERT = 5
    MENTEE_SKILL_LEVELS = (
        (NEVER_CODED_BEFORE, 'Never Coded Before'),
        (BEGINNER, 'Beginner'),
        (INTERMEDIATE, 'Intermediate'),
        (ADVANCED, 'Advanced'),
        (EXPERT, 'Expert'),
    )
    skill_level = models.PositiveSmallIntegerField(choices=MENTEE_SKILL_LEVELS, null=True, blank=True)
    grade_in_school = models.IntegerField(default=1)


    def __str__(self): 
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
