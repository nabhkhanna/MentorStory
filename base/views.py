from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib import messages
from .forms import *
from .decorators import *
from .filters import *
import random

# Create your views here.

def home(request):
    user = request.user
    context = {'user':user}
    groups = user.groups
    return render(request, 'base/index.html',context)


def aboutUs(request):
    user = request.user
    context = {'user' : user}
    return render(request, 'base/about_us.html', context)


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account Created for ' + user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'base/register.html', context)

@unauthenticated_user
def mentorRegistration(request):
    form = CreateUserForm

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            name = first_name + " " + last_name
            email = form.cleaned_data.get('email')
            group = Group.objects.get(name = 'Mentor')
            user.groups.add(group)

            Mentor.objects.create(user=user, name=name, email=email)


            messages.success(request, 'Account Created for ' + username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'base/register.html', context)

@unauthenticated_user
def menteeRegistration(request):
    form = CreateUserForm

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            name = first_name + " " + last_name
            email = form.cleaned_data.get('email')
            group = Group.objects.get(name='Mentee')
            user.groups.add(group)

            Mentee.objects.create(user=user, name=name, email=email)

            messages.success(request, 'Account Created for ' + username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'base/register.html', context)



@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
            return render(request, 'base/login.html')

    return render(request, 'base/login.html')


def lougoutUser(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def mentorProfile(request,username):
    user = User.objects.get(username = username)
    mentor = Mentor.objects.get(user = user)
    mentors = Mentor.objects.all()
    context = {'user': user,'mentor': mentor, 'mentors' : mentors}
    return render(request, 'base/userprofile.html', context)

@login_required(login_url='login')
def mentorUpdate(request):
    user = request.user
    mentor = user.mentor
    form = UpdateMentor(instance=user.mentor)

    if request.method == 'POST':
        form = UpdateMentor(request.POST, request.FILES, instance=user.mentor)
        if form.is_valid():
            form.save()

    context = {'form':form,'mentor':mentor}
    return render(request, 'base/mentor_update.html', context)

@login_required(login_url='login')
def mentorView(request,username):
    user = User.objects.get(username = username)
    mentor = Mentor.objects.get(user = user)
    mentors = Mentor.objects.all()
    context = {'mentor': mentor, 'mentors' : mentors}
    return render(request, 'base/mentorview.html', context)

@login_required(login_url='login')
def createProject(request):
    form = CreateProjectForm
    user = request.user

    if request.method == 'POST':
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            user = request.user
            project.mentor = user.mentor
            project.save()


    context = {'form': form, 'user':user}
    return render(request, 'base/create_project.html', context)

def projectView(request,id):
    user = request.user
    project = Project.objects.get(id = id)
    context = {'user' : user, 'project' : project}
    return render(request,'base/project_view.html',context)


@login_required(login_url='login')
def mentorProjectList(request):
    user = request.user
    mentor = Mentor.objects.get(user = user)
    projects = Project.objects.filter(mentor = mentor)
    context = {'projects': projects,'mentor':mentor}
    return render(request,'base/mentor_project_list.html', context)


@login_required(login_url='login')
def menteeProfile(request,username):
    user = User.objects.get(username = username)
    mentee = Mentee.objects.get(user = user)
    mentees = Mentee.objects.all()
    context = {'user': user,'mentee': mentee, 'mentees' : mentees}
    return render(request, 'base/mentee_profile.html', context)

@login_required(login_url='login')
def menteeUpdate(request):
    user = request.user
    mentee = user.mentee
    form = UpdateMentee(instance=user.mentee)

    if request.method == 'POST':
        form = UpdateMentee(request.POST, request.FILES, instance=user.mentee)
        if form.is_valid():
            form.save()

    context = {'form':form,'mentee':mentee}
    return render(request, 'base/mentee_update.html', context)

@login_required(login_url='login')
def menteeView(request,username):
    user = User.objects.get(username = username)
    mentee = Mentee.objects.get(user = user)
    mentees = Mentee.objects.all()
    context = {'mentee': mentee, 'mentees' : mentees}
    return render(request, 'base/menteeview.html', context)

@login_required(login_url='login')
def mentorFilterList(request):
    user = request.user
    mentors = Mentor.objects.all()

    myFilter = MentorFilter(request.GET, queryset=mentors)
    mentors=myFilter.qs

    context = {'mentors' : mentors,'user':user, 'myFilter':myFilter}
    return render(request, 'base/mentor_listing_filter.html', context)

@login_required(login_url='login')
def menteeFilterList(request):
    user = request.user
    mentees = Mentee.objects.all()

    myFilter = MenteeFilter(request.GET, queryset=mentees)
    mentees=myFilter.qs

    context = {'mentees' : mentees,'user':user,'myFilter':myFilter}
    return render(request, 'base/mentee_listing_filter.html', context)

@login_required(login_url='login')
def projectFilterList(request):
    projects = Project.objects.all()

    myFilter = ProjectFilter(request.GET, queryset=projects)
    projects = myFilter.qs

    context = {'projects':projects, 'myFilter': myFilter}
    return render(request, 'base/project_listing_filter.html', context)


def follow(request,username):
    user = request.user
    following = User.objects.get(username = username)
    group = None
    if request.user.groups.exists():
        group = request.user.groups.all()[0].name


    if group == 'Mentor':
        user.mentor.following.add(following)
    else:
        user.mentee.following.add(following)

    followingGroup = None
    if following.groups.exists():
        followingGroup = request.user.groups.all()[0].name

    if followingGroup == 'Mentor':
        return redirect('mentor_view', username=following.username)
    else:
        return redirect('mentee_view', username=following.username)


def follow_or_unfollow(request, username):
    owner = request.user
    to_follow = User.objects.get(username = username)

    group = None
    if owner.groups.exists():
        group = owner.groups.all()[0].name


    if group == 'Mentor':
        Followers.follow(owner,to_follow)
        owner.mentor.following.add(to_follow)
    else:
        Followers.follow(owner, to_follow)
        owner.mentee.following.add(to_follow)

    group = None
    if to_follow.groups.exists():
        group = to_follow.groups.all()[0].name

    if group == 'Mentor':
        return redirect('mentor_view', username = to_follow.username)
    else:
        return redirect('mentee_view', username = to_follow.username)

def mentor_followers_list(request, username):
    current_user = User.objects.get(username=username)
    followings = current_user.mentor.following.all()

    context = {'user ': current_user, 'followings' : followings}

    return render(request, 'base/following_list.html', context)













