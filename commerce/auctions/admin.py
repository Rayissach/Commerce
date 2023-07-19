from django.contrib import admin
from django .contrib.auth.admin import UserAdmin
from .models import User, Listing, Categories, Bids, Comments

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Listing)
admin.site.register(Categories)
admin.site.register(Bids)
admin.site.register(Comments)

