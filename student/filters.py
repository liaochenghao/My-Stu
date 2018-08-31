# coding: utf-8
import django_filters
from rest_framework.filters import FilterSet

from student.models import StudentInfo


class StudentInfoFilterSet(FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    wechat = django_filters.CharFilter(lookup_expr='icontains')
    cc = django_filters.CharFilter(lookup_expr='icontains')
    student_status = django_filters.CharFilter(lookup_expr='icontains')
    create_year = django_filters.NumberFilter(name='create_time', lookup_expr='year')

    class Meta:
        model = StudentInfo
        fields = ['name', 'email', 'wechat', 'cc', 'student_status', 'create_year']
