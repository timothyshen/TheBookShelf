#_*_ coding: utf-8 _*_

__author__ = 'Tim'
__date__ = '31/05/2021 23:23'
from django.conf import settings
from django.shortcuts import render
from django.views.generic.base import TemplateView

def inbox(request):
    context = {}
    return render(request, 'inbox/test.html', context)

class IndexTemplateView(TemplateView):
    def get_template_names(self):
        template_name = "index.html"
        return template_name