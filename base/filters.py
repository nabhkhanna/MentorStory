import django_filters
from django_filters import CharFilter

from .models import *

class MentorFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    class Meta:
        model = Mentor
        fields = ['city', 'company']


class MenteeFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    class Meta:
        model = Mentee
        fields = ['stream', 'university']


class ProjectFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')
    class Meta:
        model = Project
        fields = ['mentor', 'title', 'branch']

