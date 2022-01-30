# Generated by Django 3.2.11 on 2022-01-30 13:41

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('banner', wagtail.core.blocks.StructBlock([('banner', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('banner_title', wagtail.core.blocks.CharBlock(help_text='Banner title. Max length of 50 characters.', max_length=50)), ('banner_lead_text', wagtail.core.blocks.TextBlock(help_text='Lead text. Max length is 50 characters.', max_length=50, required=False)), ('banner_image', wagtail.images.blocks.ImageChooserBlock(help_text='Banner background image.'))])))]))], blank=True, null=True),
        ),
    ]
