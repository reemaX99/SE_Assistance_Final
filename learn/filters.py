import django_filters
from .models import learn

class LearnFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = learn
        fields = '__all__'
        exclude = ['tags','videofile','published_at','image','urlLearn','author']