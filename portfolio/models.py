from django.db import models
from wagtail.core.models import Page, Orderable
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class Portfolio(Page):

    template = "portfolio/portfolio.html"
    parent_page_types = ["home.HomePage"]
    subpage_types = []

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
