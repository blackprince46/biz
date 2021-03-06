from django.db import models
from blog.models import Company
# Create your models here.


class SupportType(models.Model):
    """
        The kind of support the customer gets, as there are some types defined for the support, and is
        provided to the customer.
    """
    type_name = models.CharField(max_length=100)
    type_desc = models.CharField(max_length=300)
    active = models.IntegerField(default=1)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)


class SubscriptionPlan(models.Model):
    """
        This is the type of subscription plans given to the end user.
    """
    plan_name=models.CharField(max_length=200)
    plan_price=models.FloatField()
    plan_benefits=models.TextField()
    plan_duration=models.CharField(max_length=250)
    max_users=models.ImageField(default=4)
    blog_limit=models.ImageField(default=10)
    support_type=models.ForeignKey(SupportType,on_delete=models.CASCADE)
    active = models.IntegerField(default=1)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

class Subscription(models.Model):
    """
        This has the information about which company have what kind of subscription plans.
    """
    com_id=models.ForeignKey(Company, on_delete=models.CASCADE,default=-1)
    plan_id=models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE,default=-1)
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()
    active = models.IntegerField(default=1)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)
