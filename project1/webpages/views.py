from django.http import HttpResponse
from django.template import loader

from .models import Webpage, Stats

# description, id, stats, title, url


def index(request):
    latest_question_list = Webpage.objects.order_by('title')[:5]
    template = loader.get_template('webpages/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
