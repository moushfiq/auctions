from django.contrib import admin
#from django.contrib.auth.models import User

from .models import Listing, Bid, Comment

admin.site.site_header = "Auction Admin"
admin.site.site_title = "Admin Portal"

# Register your models here.
#admin.site.register(User)
admin.site.register(Listing)
admin.site.register(Bid)
admin.site.register(Comment)

