from django.contrib import admin
from .models import REstate, Owner, Workgroup, Workgroup_time


@admin.register(REstate)
class REstateAdmin(admin.ModelAdmin):
    pass


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    pass


@admin.register(Workgroup)
class WorkgroupAdmin(admin.ModelAdmin):
    pass


@admin.register(Workgroup_time)
class Workgroup_timeAdmin(admin.ModelAdmin):
    pass
