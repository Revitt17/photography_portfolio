from django.db import models
from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import FieldPanel
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from django.db.models import TextField


class Portfolio(Page):

    background_home = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel('background_home'),
        MultiFieldPanel([
            InlinePanel(
                "gallery_images", 
                max_num=200, 
                min_num=1, 
                label="Image"
            ),
        ], heading="Gallery Images"),
    ]

    def get_context(self, request, *args, **kwargs):
        """ 
        Get context from "Portfolio", necessary for "projects_block",
        "banner_block" and "navbar".
        """
        context = super().get_context(request, *args, **kwargs)
        context['portfolio'] = Portfolio.objects.live().public()
        return context


class Gallery(Orderable):

    page = ParentalKey(
        Portfolio, 
        on_delete=models.CASCADE,
        related_name='gallery_images'
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        ImageChooserPanel('image'),
    ]
