from .models import Insight, Topic
import django_filters

class InsightFilter(django_filters.FilterSet):
    class Meta:
        model = Insight
        fields = ['topic',]
