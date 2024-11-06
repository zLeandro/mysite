from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "status", "get_created_at")
    list_filter = ("status",)
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}

    def get_created_at(self, obj):
        return obj.created_at

    get_created_at.admin_order_field = 'created_at'
    get_created_at.short_description = 'Created At'

admin.site.register(Post, PostAdmin)