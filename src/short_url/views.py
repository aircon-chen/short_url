# Create your views here.
from django import forms
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView

from short_url.forms import ShortUrlForm


class IndexView(CreateView):
    template_name = 'short_url/index.html'
    form_class = ShortUrlForm
    success_url = '/'
