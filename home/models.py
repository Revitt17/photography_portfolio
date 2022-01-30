from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key
from django.db import models

from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from streams import blocks
from portfolio.models import Portfolio

class HomePage(Page):
    
    parent_page_types = ["wagtailcore.Page"]
    max_count = 1

    body = StreamField([
        ("banner", blocks.BannerBlock()),
        ("about", blocks.AboutBlock()),
        ("projects", blocks.ProjectsBlock()),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel("body"),
    ]

    def get_context(self, request, *args, **kwargs):
        """ 
        Get context from "Portfolio", necessary for "projects_block",
        "banner_block" and "navbar".
        """
        context = super().get_context(request, *args, **kwargs)
        context['portfolio'] = Portfolio.objects.live().public()
        return context
