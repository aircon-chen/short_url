# Create your views here.
from django.contrib import messages
from django.urls import reverse
from django.views.generic import RedirectView, FormView
from rest_framework.generics import CreateAPIView

from short_url import serializers, forms
from short_url.models import Url


class IndexView(FormView):
    """ Index page """
    template_name = 'short_url/index.html'
    form_class = forms.ShortUrlForm


class ShortUrlAPIView(CreateAPIView):
    """ short url API """
    serializer_class = serializers.UrlSerializers


class ShortUrlRedirectView(RedirectView):
    """ Redirect url """

    def get_redirect_url(self, *args, **kwargs):
        try:

            # TODO: add the mechanism of get data from cache
            url = Url.objects.get(encode_url=kwargs['encode'])

            return url.original_url

        except Url.DoesNotExist:
            messages.error(self.request, 'short URL is not exist...')
            return reverse('index_page')
