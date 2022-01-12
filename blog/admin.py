from django.contrib import admin


from tof.admin import TofAdmin, TranslationTabularInline
from tof.decorators import tof_prefetch


# Register your models here.

from .models import Post , Category

class CategoryAdmin(TofAdmin):
    inlines = (TranslationTabularInline, )





admin.site.register(Post )
admin.site.register(Category , CategoryAdmin)