from django.contrib import admin
from .models import FutsalCompany, GroundPriceSegment, Booking

# Register your models here.
admin.site.register(FutsalCompany)
admin.site.register(GroundPriceSegment)
admin.site.register(Booking)
