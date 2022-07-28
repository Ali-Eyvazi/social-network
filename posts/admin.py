from django.contrib import admin

# Register your models here.
from .models import Post

@admin.register(Post)  # == admin.site.register(Post,PostAdmin)
class PostAdmin(admin.ModelAdmin):
    list_display=('user','slug','created','updated')
    search_fields=('slug','body')
    list_filter=('updated',)
    prepopulated_fields={'slug':('body',)}
    raw_id_fields=('user',)

    






