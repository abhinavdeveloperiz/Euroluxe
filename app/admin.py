from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.utils.html import format_html
from .models import Home, Testimonial, Product_details


# ---------- HOME ADMIN ----------
@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ("id", "banner_video_tag", "product1_image_tag", "product2_image_tag", "product3_image_tag")
    readonly_fields = ("banner_video_tag", "product1_image_tag", "product2_image_tag", "product3_image_tag")

    def banner_video_tag(self, obj):
        if obj.banner_video:
            return format_html('<video width="200" controls><source src="{}" type="video/mp4"></video>', obj.banner_video.url)
        return "No Video"
    banner_video_tag.short_description = "Banner Video"

    def product1_image_tag(self, obj):
        if obj.product1_image:
            return format_html('<img src="{}" width="100" />', obj.product1_image.url)
        return "No Image"
    product1_image_tag.short_description = "Product 1 Image"

    def product2_image_tag(self, obj):
        if obj.product2_image:
            return format_html('<img src="{}" width="100" />', obj.product2_image.url)
        return "No Image"
    product2_image_tag.short_description = "Product 2 Image"

    def product3_image_tag(self, obj):
        if obj.product3_image:
            return format_html('<img src="{}" width="100" />', obj.product3_image.url)
        return "No Image"
    product3_image_tag.short_description = "Product 3 Image"


# ---------- TESTIMONIAL ADMIN ----------
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "short_description")
    search_fields = ("name", "description")

    def short_description(self, obj):
        return obj.description[:50] + "..." if len(obj.description) > 50 else obj.description
    short_description.short_description = "Description"


# ---------- PRODUCT DETAILS ADMIN ----------
@admin.register(Product_details)
class ProductDetailsAdmin(admin.ModelAdmin):
    list_display = ("id", "image1_tag", "image2_tag", "image3_tag")
    readonly_fields = ("image1_tag", "image2_tag", "image3_tag")

    def image1_tag(self, obj):
        if obj.image1:
            return format_html('<img src="{}" width="100" />', obj.image1.url)
        return "No Image"
    image1_tag.short_description = "Image 1"

    def image2_tag(self, obj):
        if obj.image2:
            return format_html('<img src="{}" width="100" />', obj.image2.url)
        return "No Image"
    image2_tag.short_description = "Image 2"

    def image3_tag(self, obj):
        if obj.image3:
            return format_html('<img src="{}" width="100" />', obj.image3.url)
        return "No Image"
    image3_tag.short_description = "Image 3"
