from django.contrib import admin
from .models import PostUser


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")


admin.site.register(PostUser, PostAdmin)
