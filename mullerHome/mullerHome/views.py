# -*- coding: utf-8 -*-

from django.views import generic
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import io
from .models import BlogEntry


def blog_index(request):
    template = loader.get_template('mullerHome/blogBaseTemplate.html')
    context = {}
    return HttpResponse(template.render(context, request))


def blog_entry(request, entryID):
    blog_entry = get_object_or_404(BlogEntry, pk=entryID)
    template = loader.get_template('mullerHome/blogEntry.html')
    context = {
        'title': blog_entry.blog_title,
        'content': blog_entry.blog_content,
        'pub_date': blog_entry.pub_date.date().__str__(),
    }

    return HttpResponse(template.render(context, request))


def curriculum(request):
    with open('/home/muller/DjangoApps/mullerHome/mullerHome/static/mullerHome/various/MULLER_Ian_Curriculum_Vitae.pdf',
              'rb') as pdf:
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
