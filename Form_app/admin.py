from django.contrib import admin

# Register your models here.
from Form_app.models import Register

class RegisterAdmin(admin.ModelAdmin):
    list_display=['name','email','adharDetailes']
    list_display_links = ('name','email',)
    # list_editable = ('name','email',)

admin.site.register(Register,RegisterAdmin)

