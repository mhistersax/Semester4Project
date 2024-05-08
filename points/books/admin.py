from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "publication_date",
        "isbn",
        "quantity",
        "category",  # Add category field to list display
        "image_preview",
        "video_preview",
        "downloadable",
    )
    list_filter = (
        "author",
        "publication_date",
        "category",
    )  # Add category field to list filter
    search_fields = (
        "title",
        "author",
        "isbn",
        "category__name",
    )  # Add category field to search fields
    readonly_fields = ("image_preview", "video_preview")

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(
                '<img src="{url}" width="100" height="auto" />'.format(
                    url=obj.image.url
                )
            )
        else:
            return "(No image)"

    image_preview.short_description = "Image Preview"

    def video_preview(self, obj):
        if obj.video:
            return mark_safe(
                '<video width="320" height="240" controls>'
                '<source src="{url}" type="video/mp4">'
                "Your browser does not support the video tag."
                "</video>".format(url=obj.video.url)
            )
        else:
            return "(No video)"

    video_preview.short_description = "Video Preview"


admin.site.register(Book, BookAdmin)
