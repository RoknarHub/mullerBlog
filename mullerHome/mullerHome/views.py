from django.views import generic
from django.template import loader
from django.http import HttpResponse


def blogIndex(request):

    template = loader.get_template('mullerHome/blogIndex.html')
    context = {}
    return HttpResponse(template.render(context,request))


def curriculum(request):
    with open('/home/muller/DjangoApps/mullerHome/mullerHome/static/mullerHome/various/MULLER_Ian_Curriculum_Vitae.pdf', 'r') as pdf:
        response = HttpResponse(pdf.read(), mimetype='application/pdf')
        response['Content-Disposition'] = 'inline;filename=MULLER_Ian_Curriculum_Vitae.pdf'
        return response
    pdf.closed