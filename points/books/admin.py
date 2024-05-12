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
        "category",
        "book_type",  # Add book_type to list display
        "image_preview",
        "movie_details",
        "downloadable",
    )
    list_filter = (
        "author",
        "publication_date",
        "category",
        "book_type",
    )  # Add book_type to list filter
    search_fields = ("title", "author", "isbn", "category__name")
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

    def save_model(self, request, obj, form, change):
        # Check if book type is "Please select book type"
        if obj.book_type == "":
            # If book type is not selected, prevent saving
            self.message_user(
                request, "Please select a valid book type.", level="ERROR"
            )
            return
        # Otherwise, allow saving
        super().save_model(request, obj, form, change)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        book_type_field = form.base_fields.get("book_type")
        if book_type_field:
            # If the book type is 'book', remove the video field
            if obj and obj.book_type == "book":
                video_field = form.base_fields.get("video")
                if video_field:
                    video_field.required = False
                    form.base_fields.pop("video")
            # If the book type is 'video', remove the image field
            elif obj and obj.book_type == "video":
                image_field = form.base_fields.get("image")
                if image_field:
                    image_field.required = False
                    form.base_fields.pop("image")
        return form

    def movie_details(self, obj):
        if obj.movie:
            details = f"Title: {obj.movie.title}<br>"
            if obj.movie.video:
                details += (
                    f'<video width="320" height="240" controls>'
                    f'<source src="{obj.movie.video.url}" type="video/mp4">'
                    "Your browser does not support the video tag."
                    "</video>"
                )
            else:
                details += "(No video)"
            return mark_safe(details)
        else:
            return "(No movie selected)"

    movie_details.short_description = "Movie Details"


admin.site.register(Book, BookAdmin)
