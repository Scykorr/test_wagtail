from django.db import models

from wagtail.models import Page


class HomePage(Page):


    subtitle = models.CharField(max_length=255, blank=True, null=True)

