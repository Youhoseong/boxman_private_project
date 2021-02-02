from django.contrib import admin
from . import models
# Register your models here.


class PhotoInline(admin.TabularInline):
    model = models.Photo

@admin.register(models.Board)
class RoomAdmin(admin.ModelAdmin):

    inlines = (PhotoInline,)

    fieldsets = (
        (
            "Basic info",
            {
                "fields": ("title", "description", "host")
            }
        ),
    )