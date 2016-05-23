# -*- coding: utf-8 -*-

from django.views import generic
from django.template import loader
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404
import io
from .models import BlogEntry
from django.utils import timezone
from django.conf import settings


# def blog_index(request):
#     template = loader.get_template('mullerHome/blogIndex.html')
#     latest_blogs_entries = BlogEntry.objects.order_by('-pub_date')[:5]
#     context = {'latest_blogs_entries': latest_blogs_entries}
#     return HttpResponse(template.render(context, request))

class BlogIndexView(generic.ListView):
    template_name = 'mullerHome/blogIndex.html'
    context_object_name = 'latest_blog_entries'

    def get_queryset(self):
        """
        Return the last five published blog entries (not including those set to be
        published in the future).
        """
        return BlogEntry.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date').exclude(is_preview=True)[:5]


def blog_entry(request, entryID):
    blog_entry = get_object_or_404(BlogEntry, pk=entryID)
    if (blog_entry.is_preview and not request.user.is_authenticated()):
        return redirect(reverse('blogIndex'))
    template = loader.get_template('mullerHome/blogEntry.html')
    context = {
        'title': blog_entry.blog_title,
        'content': blog_entry.blog_content,
        'pub_date': blog_entry.pub_date.date().__str__(),
    }

    return HttpResponse(template.render(context, request))

def about(request):
    template = loader.get_template('mullerHome/about.html')
    context = {}
    return HttpResponse(template.render(context, request))

def curriculum(request):
    pdf = open(os.path.join(settings.STATIC_ROOT, 'mullerHome/various/MULLER_Ian_Curriculum_Vitae.pdf'),'rb').read()
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'filename=MULLER_Ian_Curriculum_Vitae.pdf'
    return response
    #redirect(reverse('mullerHome/various/MULLER_Ian_Curriculum_Vitae.pdf'))


import locale
import sys


def view_locale(request):
    loc_info = "getlocale: " + str(locale.getlocale()) + \
               "<br/>getdefaultlocale(): " + str(locale.getdefaultlocale()) + \
               "<br/>fs_encoding: " + str(sys.getfilesystemencoding()) + \
               "<br/>sys default encoding: " + str(sys.getdefaultencoding())
    "<br/>sys default encoding: " + str(sys.getdefaultencoding())
    return HttpResponse(loc_info)
