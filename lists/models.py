from django.core.urlresolvers import reverse
from django.db import models
from django.contrib import auth

import uuid

auth.signals.user_logged_in.disconnect(auth.models.update_last_login)

class List(models.Model):
    
    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])

class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)

    class Meta:
        unique_together = ('list', 'text')