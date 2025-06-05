from django.contrib import admin
from .models import Medicine, PurchaseRequest, Demand

admin.site.register(Medicine)
admin.site.register(PurchaseRequest)
admin.site.register(Demand)