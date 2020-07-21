from rest_framework import serializers

from short_url.models import Url


class UrlSerializers(serializers.ModelSerializer):
    encode_url = serializers.CharField(required=False)

    class Meta:
        model = Url
        fields = ('original_url', 'encode_url')

    def save(self, **kwargs):
        return super().save(**kwargs)
