# Create your views here.
from django.contrib import messages
from django.core.cache import cache
from django.urls import reverse
from django.views.generic import RedirectView, FormView
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from short_url import serializers, forms
from short_url.models import Url
from short_url.serializers import UrlSerializers


class IndexView(FormView):
    """ Index page """
    template_name = 'short_url/index.html'
    form_class = forms.ShortUrlForm


class ShortUrlAPIView(CreateAPIView):
    """ short url API """
    serializer_class = serializers.UrlSerializers

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_input_url = serializer.data.get('original_url')

        if Url.objects.filter(original_url=user_input_url).exists():
            url = Url.objects.filter(original_url=user_input_url).first()

            # check cache
            cache.get_or_set(url.encode_url, url.original_url)

            headers = self.get_success_headers(serializer.data)
            return Response(UrlSerializers(url).data,
                            status=status.HTTP_201_CREATED, headers=headers)

        return super().post(request, *args, **kwargs)


class ShortUrlRedirectView(RedirectView):
    """ Redirect url """

    def get_redirect_url(self, *args, **kwargs):
        try:
            original_url = cache.get(kwargs['encode'], False)
            if not original_url:
                url = Url.objects.get(encode_url=kwargs['encode'])

                # set cache
                cache.set(url.encode_url, url.original_url)

                original_url = url.original_url

            return original_url

        except Url.DoesNotExist:
            messages.error(self.request, 'short URL is not exist...')
            return reverse('index_page')
