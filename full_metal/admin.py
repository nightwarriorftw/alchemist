from django.contrib import admin
from full_metal.models import MarketingCampaign
from full_metal.models import Voucher

from reversion.admin import VersionAdmin


@admin.register(MarketingCampaign)
class MarketingCampaignAdmin(VersionAdmin):
    pass

@admin.register(Voucher)
class VoucherAdmin(VersionAdmin):
    pass
