from django.contrib import admin
from . models import News


class NewsAdmin(admin.ModelAdmin):
    fieldsets = [
            (None, {"fields": ["url"]}),
            ("Тексты", {"fields": ["title", "full_text"]}),
]
    
admin.site.register(News, NewsAdmin)