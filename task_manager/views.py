from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'
    extra_context = {'title': _('Task manager'),
                     'description': _('A simple and functional task manager.'),
                     }
