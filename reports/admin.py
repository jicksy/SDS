from django.contrib import admin
from reports.models import *

admin.site.register(Institution)
admin.site.register(Region)
admin.site.register(SubRegion)
admin.site.register(InstitutionStaff)
admin.site.register(ItemCategory)
admin.site.register(Item)
admin.site.register(Report)
admin.site.register(Visit)
admin.site.register(InstitutionPurchase)
admin.site.register(InstitutionFurtherPurchase)