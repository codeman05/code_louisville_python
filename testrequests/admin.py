from django.contrib import admin

from . import models


admin.site.register(models.Department)
admin.site.register(models.Employee)
admin.site.register(models.Customer)
admin.site.register(models.TestType)
admin.site.register(models.Test)
