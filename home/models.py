
from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldRowPanel, InlinePanel, MultiFieldPanel
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.forms.panels import FormSubmissionsPanel
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.blocks import StructBlock, CharBlock, RichTextBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.models import Image
from wagtail.images import get_image_model
from wagtail.blocks import StructBlock, CharBlock, RichTextBlock, ChoiceBlock, URLBlock
from wagtail.snippets.models import register_snippet

# -------------------------
# Three-card block
# -------------------------
class CardBlock(StructBlock):
    image = ImageChooserBlock()
    heading = CharBlock(max_length=255)
    text = RichTextBlock()
    button_text = CharBlock(max_length=100)


# -------------------------
# Customer review block
# -------------------------
class ReviewBlock(StructBlock):
    customer_name = CharBlock(max_length=255)
    review = RichTextBlock()


# -------------------------
# Blog card block
# -------------------------
class BlogBlock(StructBlock):
    image = ImageChooserBlock()
    text = RichTextBlock()
    button_text = CharBlock(max_length=100)


# -------------------------
# Homepage model
# -------------------------
class HomePage(Page):


    logo = models.ForeignKey(
        get_image_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    # Banner section
    banner_image = models.ForeignKey(
        Image,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    banner_heading = models.CharField(max_length=255, blank=True)
    banner_text = models.TextField(blank=True)
    banner_button_text = models.CharField(max_length=100, blank=True)

    # Intro section (also reused later in the template)
    intro_content = RichTextField(blank=True)

    # First image and content section
    content = RichTextField(blank=True)
    content_image = models.ForeignKey(
        Image,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    content_button_one_text = models.CharField(max_length=100, blank=True)
    content_button_two_text = models.CharField(max_length=100, blank=True)

    # Three-card section
    cards = StreamField(
        [("card", CardBlock())],
        blank=True,
        use_json_field=True,
    )

    # Second image and content section
    content_two = RichTextField(blank=True)
    content_image_two = models.ForeignKey(
        Image,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    content_button_three_text = models.CharField(max_length=100, blank=True)

    # First overlay section
    overlay_image = models.ForeignKey(
        Image,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    overlay_content = RichTextField(blank=True)
    overlay_button_text = models.CharField(max_length=100, blank=True)

    # Customer reviews section
    reviews = StreamField(
        [("review", ReviewBlock())],
        blank=True,
        use_json_field=True,
    )

    # Second overlay section
    overlay_image_two = models.ForeignKey(
        Image,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    overlay_content_two = RichTextField(blank=True)
    overlay_button_two_text = models.CharField(max_length=100, blank=True)

    # Blog cards section
    blog_cards = StreamField(
        [("blog", BlogBlock())],
        blank=True,
        use_json_field=True,
    )

    # Third overlay section
    overlay_image_three = models.ForeignKey(
        Image,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    overlay_content_three = RichTextField(blank=True)
    overlay_button_three_text = models.CharField(max_length=100, blank=True)

    # Four-image row
    image_one = models.ForeignKey(
        Image,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    image_two = models.ForeignKey(
        Image,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    image_three = models.ForeignKey(
        Image,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    image_four = models.ForeignKey(
        Image,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    # Wagtail admin panels
    content_panels = Page.content_panels + [
        FieldPanel("logo"),
        # Banner
        FieldPanel("banner_image"),
        FieldPanel("banner_heading"),
        FieldPanel("banner_text"),
        FieldPanel("banner_button_text"),

        # Intro
        FieldPanel("intro_content"),

        # First image and content section
        FieldPanel("content"),
        FieldPanel("content_image"),
        FieldPanel("content_button_one_text"),
        FieldPanel("content_button_two_text"),

        # Three-card section
        FieldPanel("cards"),

        # Second image and content section
        FieldPanel("content_two"),
        FieldPanel("content_image_two"),
        FieldPanel("content_button_three_text"),

        # First overlay
        FieldPanel("overlay_image"),
        FieldPanel("overlay_content"),
        FieldPanel("overlay_button_text"),

        # Reviews
        FieldPanel("reviews"),

        # Second overlay
        FieldPanel("overlay_image_two"),
        FieldPanel("overlay_content_two"),
        FieldPanel("overlay_button_two_text"),

        # Blog cards
        FieldPanel("blog_cards"),

        # Third overlay
        FieldPanel("overlay_image_three"),
        FieldPanel("overlay_content_three"),
        FieldPanel("overlay_button_three_text"),

        # Four-image row
        FieldPanel("image_one"),
        FieldPanel("image_two"),
        FieldPanel("image_three"),
        FieldPanel("image_four"),
    ]

# -------------------------
# Footer settings
# -------------------------
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    register_setting,
)

@register_setting
class FooterSettings(BaseGenericSetting):
    # Main footer logo
    footer_logo = models.ForeignKey(
        get_image_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    # Six trust and certification images
    amarr_logo = models.ForeignKey(
        get_image_model(), null=True, blank=True,
        on_delete=models.SET_NULL, related_name="+",
    )
    ida_logo = models.ForeignKey(
        get_image_model(), null=True, blank=True,
        on_delete=models.SET_NULL, related_name="+",
    )
    liftmaster_logo = models.ForeignKey(
        get_image_model(), null=True, blank=True,
        on_delete=models.SET_NULL, related_name="+",
    )
    made_in_usa_logo = models.ForeignKey(
        get_image_model(), null=True, blank=True,
        on_delete=models.SET_NULL, related_name="+",
    )
    recycled_steel_logo = models.ForeignKey(
        get_image_model(), null=True, blank=True,
        on_delete=models.SET_NULL, related_name="+",
    )
    bbb_logo = models.ForeignKey(
        get_image_model(), null=True, blank=True,
        on_delete=models.SET_NULL, related_name="+",
    )

    # Contact information
    contact_heading = models.CharField(
        max_length=100, default="Store To Door Service"
    )
    phone_number = models.CharField(
        max_length=50, default="1 (877) 870 DOOR (3667)"
    )
    phone_link = models.CharField(
        max_length=50, default="+18778703667"
    )
    postal_address = models.CharField(
        max_length=255,
        default="P.O. Box 498 Harrison City, PA 15636",
    )

    # Footer column headings
    resources_heading = models.CharField(
        max_length=100, default="Resources"
    )
    policies_heading = models.CharField(
        max_length=100, default="Policies & Agreements"
    )
    newsletter_heading = models.CharField(
        max_length=100, default="Stay In Touch"
    )
    newsletter_text = models.TextField(
        default=(
            "Sign up for our Newsletter to Stay Up to Date "
            "on Our Products and Monthly House Specials!"
        )
    )

    panels = [
        FieldPanel("footer_logo"),
        FieldPanel("amarr_logo"),
        FieldPanel("ida_logo"),
        FieldPanel("liftmaster_logo"),
        FieldPanel("made_in_usa_logo"),
        FieldPanel("recycled_steel_logo"),
        FieldPanel("bbb_logo"),
        FieldPanel("contact_heading"),
        FieldPanel("phone_number"),
        FieldPanel("phone_link"),
        FieldPanel("postal_address"),
        FieldPanel("resources_heading"),
        FieldPanel("policies_heading"),
        FieldPanel("newsletter_heading"),
        FieldPanel("newsletter_text"),
    ]
class ImageTextBlock(StructBlock):
    heading = CharBlock(required=False)
    text = RichTextBlock(required=False)
    image = ImageChooserBlock(required=False)
    image_position = ChoiceBlock(
        choices=[("left", "Image on left"), ("right", "Image on right")],
        default="right",
    )
    button_text = CharBlock(required=False)
    button_link = URLBlock(required=False)

    class Meta:
        icon = "image"
        label = "Image + Text Section"


class MeasuringPage(Page):
    hero_title = models.CharField(max_length=255, default="How To Measure")
    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    body = StreamField(
        [
            ("image_text", ImageTextBlock()),
            ("full_text", RichTextBlock(label="Full-width text")),
        ],
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("hero_title"),
        FieldPanel("hero_image"),
        FieldPanel("body"),
    ]

    parent_page_types = ["home.HomePage"]

@register_snippet
class GarageDoor(models.Model):
    name = models.CharField(max_length=255)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    from_price = models.CharField(max_length=20, help_text="Type the number only, e.g. 2,291.00")
    regular_price = models.CharField(max_length=20, blank=True, help_text="Optional, number only")
    on_sale = models.BooleanField(default=False)
    link = models.URLField(blank=True, help_text="Where the View Door button goes (optional)")

    panels = [
        FieldPanel("name"),
        FieldPanel("image"),
        FieldPanel("from_price"),
        FieldPanel("regular_price"),
        FieldPanel("on_sale"),
        FieldPanel("link"),
    ]

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.name


class DoorBuilderPage(Page):
    heading = models.CharField(max_length=255, default="Popular Size Garage Doors")
    bottom_heading = models.CharField(max_length=255, blank=True)
    bottom_text = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("heading"),
        FieldPanel("bottom_heading"),
        FieldPanel("bottom_text"),
    ]

    parent_page_types = ["home.HomePage"]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["doors"] = GarageDoor.objects.all()
        return context

class FAQBlock(StructBlock):
    question = CharBlock()
    answer = RichTextBlock()

    class Meta:
        icon = "help"
        label = "FAQ"


class FAQPage(Page):
    heading = models.CharField(max_length=255, default="Garage Door Discounters FAQ’s")
    intro = RichTextField(blank=True)
    faqs = StreamField([("faq", FAQBlock())], blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("heading"),
        FieldPanel("intro"),
        FieldPanel("faqs"),
    ]

    parent_page_types = ["home.HomePage"]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        items = list(self.faqs)
        half = (len(items) + 1) // 2
        context["columns"] = [
            {"id": "faqLeft", "prefix": "L", "entries": items[:half]},
            {"id": "faqRight", "prefix": "R", "entries": items[half:]},
        ]
        return context        


class CategoryCardBlock(StructBlock):
    image = ImageChooserBlock()
    title = CharBlock()
    text = RichTextBlock()
    link = URLBlock(required=False)

    class Meta:
        icon = "doc-full"
        label = "Door Card"


class DoorCategoryPage(Page):
    hero_title = models.CharField(max_length=255, default="Residential")
    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    section_heading = models.CharField(max_length=255, default="Our Residential Doors")
    cards = StreamField([("card", CategoryCardBlock())], blank=True)
    view_all_link = models.URLField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("hero_title"),
        FieldPanel("hero_image"),
        FieldPanel("section_heading"),
        FieldPanel("cards"),
        FieldPanel("view_all_link"),
    ]

    parent_page_types = ["home.HomePage"]


class CommercialFormField(AbstractFormField):
    page = ParentalKey(
        "CommercialPage",
        on_delete=models.CASCADE,
        related_name="form_fields",
    )


class CommercialPage(AbstractEmailForm):
    hero_title = models.CharField(max_length=255, default="Commercial")
    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    left_heading = models.CharField(max_length=255, default="Our Commercial Customers")
    left_text = RichTextField(blank=True)
    form_heading = models.CharField(
        max_length=255,
        default="Contact Us Today For A FREE Estimate Or To Learn About Bigger Projects",
    )
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel("hero_title"),
        FieldPanel("hero_image"),
        FieldPanel("left_heading"),
        FieldPanel("left_text"),
        FieldPanel("form_heading"),
        InlinePanel("form_fields", label="Form fields"),
        FieldPanel("thank_you_text"),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("from_address"),
                        FieldPanel("to_address"),
                    ]
                ),
                FieldPanel("subject"),
            ],
            "Email",
        ),
    ]

    parent_page_types = ["home.HomePage"]

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        placeholders = {
            "street_address": "Street Address",
            "address_line_2": "Address Line 2",
            "city": "City",
            "state_province_region": "State / Province / Region",
            "zip_postal_code": "ZIP / Postal Code",
            "country": "Country",
            "comments": "Message",
        }
        for name, field in form.fields.items():
            field.widget.attrs["class"] = "form-control"
            if name in placeholders:
                field.widget.attrs["placeholder"] = placeholders[name]
            if name == "comments":
                field.widget.attrs["rows"] = 4
        return form    

class SpecialsPage(Page):
    hero_title = models.CharField(max_length=255, default="Specials")
    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    heading = models.CharField(
        max_length=255,
        default="Current Discounts On Heritage & Classica Model Garage Doors",
    )
    subheading = models.CharField(
        max_length=255,
        blank=True,
        default="Customize and Price Your Door Now!",
    )
    subheading_link = models.URLField(
        blank=True,
        help_text="Optional. If filled, the green line becomes a link.",
    )

    content_panels = Page.content_panels + [
        FieldPanel("hero_title"),
        FieldPanel("hero_image"),
        FieldPanel("heading"),
        FieldPanel("subheading"),
        FieldPanel("subheading_link"),
    ]

    parent_page_types = ["home.HomePage"]


class ContactFormField(AbstractFormField):
    page = ParentalKey(
        "ContactPage",
        on_delete=models.CASCADE,
        related_name="form_fields",
    )


class ContactPage(AbstractEmailForm):
    hero_title = models.CharField(max_length=255, default="Contact Us")
    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    left_heading = models.CharField(max_length=255, default="Contact Us")
    left_text = RichTextField(blank=True)
    form_heading = models.CharField(max_length=255, default="Have A Question?")
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel("hero_title"),
        FieldPanel("hero_image"),
        FieldPanel("left_heading"),
        FieldPanel("left_text"),
        FieldPanel("form_heading"),
        InlinePanel("form_fields", label="Form fields"),
        FieldPanel("thank_you_text"),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("from_address"),
                        FieldPanel("to_address"),
                    ]
                ),
                FieldPanel("subject"),
            ],
            "Email",
        ),
    ]

    parent_page_types = ["home.HomePage"]

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        placeholders = {
            "name": "Name",
            "email": "Email",
            "phone": "Phone",
            "message": "Message",
        }
        for name, field in form.fields.items():
            field.widget.attrs["class"] = "form-control"
            if name in placeholders:
                field.widget.attrs["placeholder"] = placeholders[name]
            if name == "message":
                field.widget.attrs["rows"] = 6
        return form            