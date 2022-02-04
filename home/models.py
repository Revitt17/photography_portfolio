from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from streams import blocks
from portfolio.models import Portfolio


class HomePage(Page):
    
    template = "home/home_page.html"
    parent_page_types = ["wagtailcore.Page"]
    subpage_types = ["portfolio.Portfolio"]
    max_count = 1

    body = StreamField([
        ("banner", blocks.BannerBlock()),
        ("about", blocks.AboutBlock()),
        ("projects", blocks.ProjectsBlock()),
        ("contact", blocks.ContactBlock()),
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
