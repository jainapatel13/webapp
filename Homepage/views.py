from django.shortcuts import render, HttpResponse
from django.template import RequestContext
from django.template.loader import get_template


def Homepage(request):
    template = get_template('Data.html')
    variables = RequestContext(request, {'user': request.user})
    output = template.render(variables)
    return HttpResponse(output)