from django.contrib import admin
from .models import DrugType, Manufacturer, DrugComposition, Drug, DataSource, PackSizeLabel

admin.site.register(Manufacturer)
admin.site.register(PackSizeLabel)
admin.site.register(DrugComposition)
admin.site.register(DataSource)
admin.site.register(Drug)
admin.site.register(DrugType)
