from django.contrib import admin
from listings.models import Band,Listings
# Register your models here.

class AdminBand(admin.ModelAdmin):
    list_display=('name','year_formed','genre')

admin.site.register(Band,AdminBand)

class ListingAdmin(admin.ModelAdmin):
      list_display = ('title', 'band')# add 'band' here

admin.site.register(Listings,ListingAdmin)