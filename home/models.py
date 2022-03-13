from django.db import models
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from portfolio.models import Portfolio


class HomePage(Page):
    
    template = "home/home_page.html"
    parent_page_types = ["wagtailcore.Page"]
    subpage_types = ["portfolio.Portfolio"]
    max_count = 1

    # Hero Section
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        related_name='+',
        on_delete=models.SET_NULL,
    )
    hero_mask = models.CharField(
        max_length=4,
        blank=False,
        null=True,
        help_text="Enter number from '0' to 1000' for change mask"
    )
    hero_title = models.CharField(
        max_length=140,
        blank=False,
        null=True,
    )
    hero_lead_text = models.CharField(
        max_length=140,
        blank=False,
        null=True,
    )

    # About Section
    about_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        related_name='+',
        help_text="Vertical profile image 3x2 aspect ratio",
        on_delete= models.SET_NULL,
    )
    about_title = models.CharField(
        max_length=140,
        blank=False,
        null=True,
    )
    about_lead_text = models.CharField(
        max_length=140,
        blank=False,
        null=True,
    )
    about_first_paragrapher = models.TextField(
        blank=False,
        max_length=500,
        null=True,
    )
    about_second_paragrapher = models.TextField(
        blank=True,
        max_length=500,
        null=True,
    )

    # Work Section
    portfolio_title = models.CharField(
        max_length=140,
        blank=False,
        null=True,
    )
    portfolio_lead_text = models.TextField(
        blank=True,
        max_length=500,
        null=True,
    )

    # Contact Section
    contact_section_title = models.CharField(
        max_length=140,
        blank=False,
        null=True,
    )
    contact_lead_text = models.TextField(
        blank=False,
        max_length=500,
        null=True,
    )
    social_network_title = models.CharField(
        max_length=140,
        blank=False,
        null=True,
    )
    contact_email_title = models.CharField(
        max_length=140,
        blank=False,
        null=True,
    )
    contact_email = models.TextField(
        blank=False,
        max_length=500,
        null=True,
    )
    contact_phone_title = models.CharField(
        max_length=140,
        blank=False,
        null=True,
    )
    contact_phone = models.TextField(
        blank=False,
        max_length=500,
        null=True,
    )
    

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            ImageChooserPanel("hero_image"),
            FieldPanel("hero_mask"),
            FieldPanel("hero_title"),
            FieldPanel("hero_lead_text"),
        ], heading="Hero Section"),
        MultiFieldPanel([
            ImageChooserPanel("about_image"),
            FieldPanel("about_title"),
            FieldPanel("about_lead_text"),
            FieldPanel("about_first_paragrapher"),
            FieldPanel("about_second_paragrapher"),
        ], heading="About Section"),
        MultiFieldPanel([
            FieldPanel("portfolio_title"),
            FieldPanel("portfolio_lead_text"),
        ], heading="Work Section"),
        MultiFieldPanel([
            FieldPanel("contact_section_title"),
            FieldPanel("contact_lead_text"),
            FieldPanel("social_network_title"),
            FieldPanel("contact_email_title"),
            FieldPanel("contact_email"),
            FieldPanel("contact_phone_title"),
            FieldPanel("contact_phone"),
        ], heading="Contact Section"),
    ]

    def get_context(self, request, *args, **kwargs):
        """ 
        Get context from "Portfolio", necessary for "hero_section" and
        "work_section".
        """
        context = super().get_context(request, *args, **kwargs)
        context['portfolio'] = Portfolio.objects.live().public()
        return context
