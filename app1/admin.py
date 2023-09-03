from django.contrib import admin
from . import models as m
# Register your models here.


admin.site.register(m.Customer_Info)
admin.site.register(m.Admin_Info)
admin.site.register(m.Dealer_Registration)
admin.site.register(m.Jewellery_Info)
admin.site.register(m.Order_Info)
admin.site.register(m.Cart_Info)
admin.site.register(m.Payment_Info)
admin.site.register(m.Invoice)
admin.site.register(m.Wishlist)
admin.site.register(m.Feedback)
admin.site.register(m.Category_Info)