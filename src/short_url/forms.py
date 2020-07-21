from django import forms

from short_url.models import Url


class ShortUrlForm(forms.ModelForm):

    class Meta:
        model = Url
        fields = ('original_url',)
