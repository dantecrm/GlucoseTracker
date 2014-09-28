from django.contrib import admin

from glucoses.models import Glucose, Category, Unit

admin.site.register(Glucose)
admin.site.register(Category)
admin.site.register(Unit)
