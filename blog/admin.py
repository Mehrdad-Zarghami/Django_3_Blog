from django.contrib import admin
from .models import PostModel


@admin.register(PostModel)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'datatime_create', 'datetime_modified', 'status',)
    ordering = ('status', '-datetime_modified',)


# class PostAdmin(admin.ModelAdmin):
#     # a tuple or list of columns that we want to be showed in the admin panel in PostModel table
#     list_display = ('title', 'author', 'datatime_create', 'datetime_modified', 'status',)
#
#     # a tuple or list of columns that determine the order of records in admin panel. the "-" sign make
#     # the ascending order into descending
#     ordering = ('status', '-datetime_modified',)
#
#
# admin.site.register(PostModel, PostAdmin)
#
