import sys
import uuid

from django.core.cache import cache
from django.db import models
from django.utils.baseconv import base62


class Url(models.Model):
    original_url = models.URLField()
    encode_url = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # Add UUID ensure every single url generate unique hash value.
        hash_val = hash('%s_%s' % (uuid.uuid1(), self.original_url))

        # Make sure hash value is positive
        hash_val %= ((sys.maxsize + 1) * 2)

        # Cast hash value to base62 encoding
        base62_val = base62.encode(hash_val)

        # Take part of encoding string to represent a unique short link
        self.encode_url = base62_val[:7]

        super().save(force_insert, force_update, using, update_fields)

        print('set cache...')
        cache.set(self.encode_url, self.original_url)

