from django.db import models
from django.utils.baseconv import base62


class Url(models.Model):
    original_url = models.URLField()
    encode_url = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        hash_val = hash(self.original_url)
        print('hash_val: %s' % hash_val)
        base62_val = base62.encode(hash_val)
        print('encode: %s' % base62_val)
        self.encode_url = base62_val
        super().save(force_insert, force_update, using, update_fields)
