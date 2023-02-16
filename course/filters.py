import django_filters
from .models import course

class CourseFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = course
        fields = '__all__'
        exclude = ['CRN_num','published_at','image','facality_members','requirment']