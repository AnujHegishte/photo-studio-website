from django.contrib import admin
from .models import FbModel

class FbAdmin(admin.ModelAdmin):
    list_display=("name", "crdt")
    list_filter=("crdt",)

admin.site.register(FbModel,FbAdmin)

