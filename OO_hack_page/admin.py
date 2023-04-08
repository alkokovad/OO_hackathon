from django.contrib import admin
from .models import REstate, Owner


@admin.register(REstate)
class REstateAdmin(admin.ModelAdmin):
    pass


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    pass
