from django.shortcuts import render
from .models import Section, Insight, Topic


# Create your views here.


def home(request):
    return render (request, 'core/index.html')

def insight(request, topic):
    print(topic)
    if topic == "Latest":
        insight = Insight.objects.all()
    else: 
        insight = Insight.objects.filter(topic__name__startswith=topic).all()
        
    topic_count = Topic.objects.all().count()
    section_count = Section.objects.all().count()
    filter_count  = topic_count + section_count
    sections=Section.objects.all()
    # insight = Insight.objects.all()
    topics = Topic.objects.all().order_by('name').values()
    

    context={
        'filter_count': filter_count,
        'topics' :topics,
        'sections':sections,
        'insights':insight,
        'topic':topic,
    }
    return render (request, 'core/insight.html', context)