from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting


@register_setting
class NavbarSettings(BaseSetting):

    brand = models.CharField(
        max_length=50,
        blank=False,
        null=True,
        help_text='Enter your Brand, it will appear on the navbar' 
    )
    about = models.CharField(
        max_length=50,
        blank=False,
        null=True,
        help_text='Choose how to call the link for "About" section in navabar'
    )
    portfolio = models.CharField(
        max_length=50,
        blank=False,
        null=True,
        help_text='Choose how to call the link for "Portfolio" page in navabar'
    )
    contact = models.CharField(
        max_length=50,
        blank=False,
        null=True,
        help_text='Choose how to call the link for "Contact" section in navabar'
    )

    panels = [
        FieldPanel("brand"),
        FieldPanel("about"),
        FieldPanel("portfolio"),
        FieldPanel("contact"),
    ]


@register_setting
class FooterSettings(BaseSetting):

    back_to_top = models.CharField(
        max_length=50,
        blank=False,
        null=True,
        help_text='Choose how to call the link for "Back to top" in footer' 
    )

    panels = [
        FieldPanel("back_to_top"),
    ]


@register_setting
class SocialMediaSettings(BaseSetting):

    vk = models.URLField(
        blank=True,
        help_text='Enter your Vk URL'
    )
    facebook = models.URLField(
        blank=True,
        help_text='Enter your Facebook URL'
    )
    instagram = models.URLField(
        blank=True,
        help_text='Enter your Instagram URL'
    )
    twitter =  models.URLField(
        blank=True,
        help_text='Enter your Twitter URL'
    )
    tiktok = models.URLField(
        blank=True,
        help_text='Enter your TikTok URL'
    )
    github = models.URLField(
        blank=True,
        help_text='Enter your GitHub URL'
    )
    linkedin = models.URLField(
        blank=True,
        help_text='Enter your LinkedIn URL'
    )
    youtube = models.URLField(
        blank=True,
        help_text='Enter your Youtube URL'
    )
    whatsapp = models.URLField(
        blank=True,
        help_text='Enter your Whatsapp URL'
    )
    telegram = models.URLField(
        blank=True,
        help_text='Enter your Telegram URL'
    )
  
    panels = [
        FieldPanel("vk"),
        FieldPanel("facebook"),
        FieldPanel("instagram"),
        FieldPanel("twitter"),
        FieldPanel("tiktok"),
        FieldPanel("github"),
        FieldPanel("linkedin"),
        FieldPanel("youtube"),
        FieldPanel("whatsapp"),
        FieldPanel("telegram"),        
    ]