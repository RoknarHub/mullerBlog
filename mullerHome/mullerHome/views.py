# -*- coding: utf-8 -*-

from django.views import generic
from django.template import loader
from django.http import HttpResponse
import io


def blogIndex(request):

    template = loader.get_template('mullerHome/blogIndex.html')
    context = {}
    return HttpResponse(template.render(context,request))


def curriculum(request):
    with open('/home/muller/DjangoApps/mullerHome/mullerHome/static/mullerHome/various/MULLER_Ian_Curriculum_Vitae.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=MULLER_Ian_Curriculum_Vitae.pdf'
        return response
    pdf.closed


import locale
import sys


def view_locale(request):
    loc_info = "getlocale: " + str(locale.getlocale()) + \
               "<br/>getdefaultlocale(): " + str(locale.getdefaultlocale()) + \
               "<br/>fs_encoding: " + str(sys.getfilesystemencoding()) + \
               "<br/>sys default encoding: " + str(sys.getdefaultencoding())
    "<br/>sys default encoding: " + str(sys.getdefaultencoding())
    return HttpResponse(loc_info)