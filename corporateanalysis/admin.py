from django.contrib import admin
from .models import Company, Data


# Register your models here.
class EdinetModelAdmin(admin.ModelAdmin):
    list_display = ('company', 'data')
    fields = ('company', 'data')


admin.site.register(Company)
admin.site.register(Data)
