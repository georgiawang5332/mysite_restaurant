from django.contrib import admin
from .models import *


# Register your models here.
# admin.site.register(UserProfile)  # 店家(餐廳)


class UserProfileAdmin(admin.ModelAdmin):
  list_display = ('user', 'user_info', 'city', 'phone', 'website', 'image')

  def user_info(self, obj):
    return obj.description
  user_info.short_description = '高端資訊'

  def get_queryset(self, request):
    queryset = super(UserProfileAdmin, self).get_queryset(request)
    queryset = queryset.order_by('-phone', 'user')
    return queryset


admin.site.register(UserProfile, UserProfileAdmin)


# admin.site.site_header = 'Adminnnnnn'  # 店家(餐廳)admin.site.site_header = 'My admin'
# admin.site.index_title = 'Features area'                 # default: "Site administration"
# admin.site.site_title = 'HTML title from adminsitration' # default: "Django site admin"

class MenuItemInline(admin.StackedInline):
  model = MenuItem
  extra = 1


class MenuItemAdmin(admin.ModelAdmin):
  list_display = ('menuItem_name', 'menuItem_price', 'menuItem_meals_size', 'menuItem_store', 'menuItem_notes')
  list_filter = ('menuItem_name',)
  search_fields = ('menuItem_name',)
  fields = ('menuItem_name', 'menuItem_price', 'menuItem_meals_size', 'menuItem_store',
            'menuItem_notes')  # 這將會使得price欄位出現在restaurant欄位之前，而且name、is_spicy和comment欄位都不會出現，不能被編輯。
  ordering = ('-menuItem_price',)


admin.site.register(MenuItem, MenuItemAdmin)  # 菜單


class StoreAdmin(admin.ModelAdmin):
  list_display = ('store_name', 'store_holder', 'store_phoneNumber', 'store_address', 'store_email', 'store_notes')
  inlines = (MenuItemInline,)
  list_filter = ('store_name',)
  search_fields = ('store_name',)
  fields = ('store_name', 'store_holder', 'store_phoneNumber',
            'store_address', 'store_email')  # 這將會使得price欄位出現在restaurant欄位之前，而且name、is_spicy和comment欄位都不會出現，不能被編輯。


admin.site.register(Store, StoreAdmin)  # 店家(餐廳)


class IngredientsInline(admin.StackedInline):
  model = Ingredients
  extra = 1


class IngredientsAdmin(admin.ModelAdmin):
  list_display = (
    'ingredients_name', 'ingredients_price', 'ingredients_unit', 'ingredients_vendor', 'ingredients_notes')
  list_filter = ('ingredients_name',)
  search_fields = ('ingredients_name',)
  fields = ('ingredients_name', 'ingredients_price', 'ingredients_unit', 'ingredients_vendor',
            'ingredients_notes')  # 這將會使得price欄位出現在restaurant欄位之前，而且name、is_spicy和comment欄位都不會出現，不能被編輯。
  ordering = ('-ingredients_price',)


admin.site.register(Ingredients, IngredientsAdmin)  # 菜單


class VendorAdmin(admin.ModelAdmin):
  list_display = ('vendor_store_name', 'vendor_holder_name', 'vendor_phone_number', 'vendor_address', 'vendor_notes')
  inlines = (IngredientsInline,)
  list_filter = ('vendor_store_name',)
  search_fields = ('vendor_store_name',)
  fields = ('vendor_store_name', 'vendor_holder_name', 'vendor_phone_number',
            'vendor_address', 'vendor_notes')  # 這將會使得price欄位出現在restaurant欄位之前，而且name、is_spicy和comment欄位都不會出現，不能被編輯。


admin.site.register(Vendor, VendorAdmin)  # 店家(餐廳)
