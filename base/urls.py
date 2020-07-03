from django.contrib import admin
from django.urls import path,include
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name= 'home'),
    path('aboutus/', views.aboutUs, name='about_us'),
    path('register', views.registerPage, name='register'),
    path('mentorreg', views.mentorRegistration, name = 'mentor_reg'),
    path('menteereg', views.menteeRegistration, name='mentee_reg'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.lougoutUser, name='logout'),

    path('mentordashboard/<username>/', views.mentorProfile, name='mentor_dashboard'),
    path('mentorupdate/', views.mentorUpdate, name='mentor_update'),
    path('mentorview/<username>/', views.mentorView, name='mentor_view'),
    path('mentorfollowing/<username>',views.mentor_followers_list, name='mentorfollowing'),

    path('createproject/', views.createProject, name='create_project'),
    path('projectlist/', views.mentorProjectList,name='project_list'),
    path('projectview/<int:id>/',views.projectView, name='project_view'),

    path('menteedashboard/<username>', views.menteeProfile,name='mentee_dashboard'),
    path('menteeupdate/', views.menteeUpdate,name='mentee_update'),
    path('menteeview/<username>/', views.menteeView, name='mentee_view'),

    path('mentorlistfilter/',views.mentorFilterList, name='mentor_list_filter'),
    path('menteelistfilter/',views.menteeFilterList, name='mentee_list_filter'),
    path('projectlistfilter/',views.projectFilterList, name='project_list_filter'),

    path('follow/<username>/', views.follow_or_unfollow, name='follow_unfollow'),

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
