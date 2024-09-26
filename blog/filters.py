import django_filters
from .models import Blog


class BlogFilter(django_filters.FilterSet):
    class Meta:
        model = Blog
        fields = ['title', 'body']
        filter_overrides = {
            'tags': django_filters.CharFilter(field_name='tags__slug', lookup_expr='exact'),
        }
