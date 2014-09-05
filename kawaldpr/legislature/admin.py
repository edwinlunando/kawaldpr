from django.contrib import admin
from models import Legislature, Medium


class LegislatureAdmin(admin.ModelAdmin):

    model = Legislature


class MediumAdmin(admin.ModelAdmin):

    model = Medium


admin.site.register(Legislature, LegislatureAdmin)
admin.site.register(Medium, MediumAdmin)
