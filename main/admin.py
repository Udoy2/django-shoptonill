from django.contrib import admin
from .models import GroupCommitte, Gallery, Shobhapoti, Contact
from django.utils.html import format_html

# Register your models here.


class AdminCommitte(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" height="{}" />'.format(
            obj.profile_pic.url, '100'))

    image_tag.short_description = 'profile pic'
    list_display = ['image_tag', 'full_name', 'designation']


class AdminGallery(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" height="{}" />'.format(
            obj.gallery_pic.url, '100'))

    image_tag.short_description = 'Gallery image'

    list_display = [
        'image_tag',
    ]


class AdminShobhapoti(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" height="{}" />'.format(
            obj.profile_pic.url, '100'))

    image_tag.short_description = 'Shobhapoti profile pic'

    list_display = [
        'image_tag',
    ]


class AdminContact(admin.ModelAdmin):
    list_display = ['name', 'email']


admin.site.register(GroupCommitte, AdminCommitte)
admin.site.register(Gallery, AdminGallery)
admin.site.register(Shobhapoti, AdminShobhapoti)
admin.site.register(Contact, AdminContact)
