from django.shortcuts import render
from .models import Section, Insight, Topic
from .filters import InsightFilter

# Create your views here.


def home(request):
    return render (request, 'core/index.html')

def insight(request, id):
    print(id)
    if id == "Latest":
        insight = Insight.objects.all()
    else: 
        insight = Insight.objects.filter(topic=id).all()
        
    topic_count = Topic.objects.all().count()
    section_count = Section.objects.all().count()
    filter_count  = topic_count + section_count
    sections=Section.objects.all()
    insight = Insight.objects.all()
    topics = Topic.objects.all().order_by('name').values()
    

    context={
        'filter_count': filter_count,
        'topics' :topics,
        'sections':sections,
        'insights':insight,
        'topic':id,
    }
    return render (request, 'core/insight.html', context)