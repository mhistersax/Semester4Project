# admin.py
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
        "image_preview",
        "downloadable",
    )
    list_filter = ("author", "publication_date")
    search_fields = ("title", "author", "isbn")
    readonly_fields = ("image_preview",)

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


admin.site.register(Book, BookAdmin)
