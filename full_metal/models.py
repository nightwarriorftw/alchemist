from django.db import models
from django.db.models.fields import related


class MarketingCampaign(models.Model):
    """Store the information of marketing campaign."""
    
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'<Marketing Campaign: {self.title}>'


class Voucher(models.Model):
    """Store the information of the voucher."""
    
    campaign = models.ForeignKey(MarketingCampaign, on_delete=models.CASCADE, related_name="campaign")
    code = models.CharField(max_length=15)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        active = "Yes" if self.active else "No"
        return f"<Voucher: {self.code} ({active})>"