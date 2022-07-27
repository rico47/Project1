from django.http import HttpResponse
from django.template import loader

from .models import Webpage, Stats

# description, id, stats, title, url


def navbar(request):
    latest_question_list = Webpage.objects.order_by('title')[:5]
    template = loader.get_template('webpages/navbar.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def index(request):
    pass

