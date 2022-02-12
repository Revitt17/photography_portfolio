# Generated by Django 4.0 on 2022-02-12 14:12

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_homepage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('banner', wagtail.core.blocks.StructBlock([('banner', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('banner_title', wagtail.core.blocks.CharBlock(help_text='Banner title. Max length of 50 characters.', max_length=50)), ('banner_lead_text', wagtail.core.blocks.TextBlock(help_text='Lead text. Max length is 50 characters.', max_length=50, required=False)), ('banner_image', wagtail.images.blocks.ImageChooserBlock(help_text='Banner background image.'))])))])), ('about', wagtail.core.blocks.StructBlock([('about', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('about_title', wagtail.core.blocks.CharBlock(help_text='About section title. Max length of 50 characters.', max_length=50)), ('about_lead_text', wagtail.core.blocks.CharBlock(help_text='Lead text. Max length is 200 characters.', max_length=200, required=False)), ('about_image', wagtail.images.blocks.ImageChooserBlock(help_text='About profile image.')), ('first_paragrapher', wagtail.core.blocks.TextBlock(help_text='First paragrapher. Max length is 500 characters.', max_length=500, required=False)), ('second_paragrapher', wagtail.core.blocks.TextBlock(help_text='Second paragrapher. Max length is 500 characters.', max_length=500, required=False))])))])), ('projects', wagtail.core.blocks.StructBlock([('projects', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('projects_title', wagtail.core.blocks.CharBlock(help_text='Projects section title. Max length of 50 characters.', max_length=50)), ('projects_lead_text', wagtail.core.blocks.TextBlock(help_text='Lead text. Max length is 50 characters.', max_length=50, required=False))])))])), ('contact', wagtail.core.blocks.StructBlock([('contact', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('contact_section_title', wagtail.core.blocks.CharBlock(help_text='Contact section title. Max length is 50 characters.', max_length=50)), ('contact_lead_text', wagtail.core.blocks.CharBlock(help_text='Lead text. Max length is 500 characters.', max_length=500, required=False)), ('contact_title', wagtail.core.blocks.TextBlock(help_text='Contact section title. Max length is 50 characters.', max_length=50, required=False)), ('contact_phone', wagtail.core.blocks.TextBlock(help_text="Format = 'Phone: +0123456789' ", max_length=100, required=False)), ('contact_email', wagtail.core.blocks.TextBlock(help_text="Format = 'Email: email@email.com' ", max_length=100, required=False)), ('contact_whatsapp', wagtail.core.blocks.URLBlock(help_text='Enter your Whatsapp url.', max_length=200, required=False)), ('contact_telegram', wagtail.core.blocks.URLBlock(help_text='Enter your Telegram url.', max_length=200, required=False)), ('social_network_title', wagtail.core.blocks.TextBlock(help_text='Title social networks section.', max_length=50, required=False)), ('contact_vk', wagtail.core.blocks.URLBlock(help_text='Enter your VK url.', max_length=200, required=False)), ('contact_instagram', wagtail.core.blocks.URLBlock(help_text='Enter your Instagram url.', max_length=200, required=False)), ('contact_tiktok', wagtail.core.blocks.URLBlock(help_text='Enter your TikTok url.', max_length=200, required=False))])))]))], blank=True, null=True),
        ),
    ]
