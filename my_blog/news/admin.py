from django.contrib import admin
from .models import Post


# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'publish', 'status']
    list_filter = ['status', 'created', 'publish']
    search_fields = ['title', 'body']
    # prepopulated_fields = {'slug': ['title']}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    # raw_id_fields = ['author']
    show_facets = admin.ShowFacets.ALWAYS