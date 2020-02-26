from django.contrib import admin
from subscription.models import SupportType, SubscriptionPlan, Subscription

# Register your models here.

class SupportTypeAdmin(admin.ModelAdmin):
    pass

# Instead of this, we can use a decorator.
admin.site.register(SupportType, SupportTypeAdmin)


class SubscriptionAdmin(admin.ModelAdmin):
    pass

# Instead of this, we can use a decorator.
admin.site.register(Subscription, SubscriptionAdmin)


class SubscriptionPlanAdmin(admin.ModelAdmin):
    pass

# Instead of this, we can use a decorator.
admin.site.register(SubscriptionPlan, SubscriptionPlanAdmin)