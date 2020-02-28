from django.contrib import admin


# Register your models here.
from pricing.models import PricingPlan


class PricingPlanAdmin(admin.ModelAdmin):
    pass


admin.site.register(PricingPlan, PricingPlanAdmin)
