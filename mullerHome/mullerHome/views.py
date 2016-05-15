from django.views import generic
from django.template import loader
from django.http import HttpResponse


def blogIndex(request):

    template = loader.get_template('mullerHome/blogIndex.html')
    context = {}
    return HttpResponse(template.render(context,request))