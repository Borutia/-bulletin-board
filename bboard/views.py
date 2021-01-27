from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Bb, Rubric
from .forms import BbForm


def index(request):
    template = 'bboard/index.html'
    bboards = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {
        'bboards': bboards,
        'rubrics': rubrics,
    }
    return render(request, template, context)


def by_rubric(request, rubric_id):
    bboards = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {
        'bboards': bboards,
        'rubrics': rubrics,
        'current_rubric': current_rubric
    }
    return render(request, 'bboard/by_rubric.html', context)


class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context
