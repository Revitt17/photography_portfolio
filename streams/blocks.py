from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class Banner(blocks.StructBlock):

    banner_title = blocks.CharBlock(
        max_length=50,
        help_text="Banner title. Max length of 50 characters.",
    )
    banner_lead_text = blocks.TextBlock(
        max_length=50,
        help_text="Lead text. Max length is 50 characters.",
        required=False
    )
    banner_image = ImageChooserBlock(
        help_text="Banner background image."
    )


class BannerBlock(blocks.StructBlock):

    banner = blocks.ListBlock(
        Banner()
    )

    class Meta:
        template = "home/banner_block.html"
        icon = "image"
        label = "Banner"


class About(blocks.StructBlock):

    about_title = blocks.CharBlock(
        max_length=50,
        help_text="About section title. Max length of 50 characters.",
    )
    about_lead_text = blocks.CharBlock(
        max_length=50,
        help_text="Lead text. Max length is 50 characters.",
        required=False
    )
    about_image = ImageChooserBlock(
        help_text="About profile image."
    )
    first_paragrapher = blocks.TextBlock(
        max_length=50,
        help_text="First paragrapher. Max length is 500 characters.",
        required=False
    )
    second_paragrapher = blocks.TextBlock(
        max_length=50,
        help_text="Second paragrapher. Max length is 500 characters.",
        required=False
    )


class AboutBlock(blocks.StructBlock):

    about = blocks.ListBlock(
        About()
    )

    class Meta:
        template = "home/about_block.html"
        icon = "image"
        label = "About"


class Projects(blocks.StructBlock):

    projects_title = blocks.CharBlock(
        max_length=50,
        help_text="Projects section title. Max length of 50 characters.",
    )
    projects_lead_text = blocks.TextBlock(
        max_length=50,
        help_text="Lead text. Max length is 50 characters.",
        required=False
    )


class ProjectsBlock(blocks.StructBlock):

    projects = blocks.ListBlock(
        Projects()
    )

    class Meta:
        template = "home/projects_block.html"
        icon = "image"
        label = "projects"
