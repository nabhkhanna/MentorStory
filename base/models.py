import datetime

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Followers(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='owner', null = True, on_delete=models.CASCADE)

    def __str__(self):
        return '{} followers'.format(self.current_user)

    @classmethod
    def follow(cls,current_user, to_follow):
        friend, created = cls.objects.get_or_create(current_user=current_user)
        friend.users.add(to_follow)

    @classmethod
    def unfollow(cls, current_user, to_follow):
        friend, created = cls.objects.get_or_create(current_user=current_user)
        friend.users.remove(to_follow)


class Mentor(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, default="mentor first name")
    job_title = models.CharField(max_length=100, null=True, blank=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    street1 = models.CharField(max_length=100, null=True, blank=True)
    street2 = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    photo = models.ImageField(null=True, default='static/userpictures/default.jpg', blank=True)
    cover_photo = models.ImageField(null=True, default='static/userpictures/defaultcover.jpg', blank=True)
    resume = models.FileField(null=True, blank=True)
    phone = models.CharField(max_length=200, null = True, blank=True)
    email = models.CharField(max_length=200, null = True, blank=True)
    birthday = models.DateField(default=datetime.date.today, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    following = models.ManyToManyField(User,symmetrical=False, related_name='mentorfollowing', blank=True)
    def get_absolute_url(self):
        return reverse('mentor_view', kwargs={"username" : self.user.username})




    def __str__(self):
        return self.name


class Mentee(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, default="mentee first name")
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    birthday = models.DateField(default=datetime.date.today, blank=True)
    university = models.CharField(max_length=200, null=True, blank=True)
    stream = models.CharField(max_length=200, null=True, blank=True)
    photo = models.ImageField(null=True, default='static/userpictures/default.jpg', blank=True)
    cover_photo = models.ImageField(null=True, default='static/userpictures/defaultcover.jpg', blank=True)
    resume = models.FileField(null=True, blank=True)
    motivation = models.CharField(max_length=500, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    following = models.ManyToManyField(User, symmetrical=False, related_name='menteefollowing',  blank=True)


    def get_absolute_url(self):
        return reverse('mentee_view', kwargs={"username" : self.user.username})


    def __str__(self):
        return self.name

class Project(models.Model):
    ranks = [
        ('Bachlor', 'Bachelor'),
        ('Master', 'Master'),
        ('PHD', 'PHD'),
    ]
    mentor = models.ForeignKey(Mentor,null=True,on_delete=models.SET_NULL, blank=True)
    mentee = models.ForeignKey(Mentee, null=True, on_delete=models.SET_NULL, blank=True)
    title = models.CharField(max_length=200,null=True, blank=True)
    required_tools = models.CharField(max_length=200,null=True, blank=True)
    branch = models.CharField(max_length=200, null=True, blank=True)
    suitable_for = models.CharField(max_length=200, null=True, choices=ranks, blank=True)
    description = models.CharField(max_length=2000, null=True, blank=True)
    taken = models.BooleanField(default=False, blank=True)
    completed = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project_view', kwargs={"id" : self.id})












