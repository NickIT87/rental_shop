from django.contrib import admin
from .models import Realtor, Apartment, ApartmentGallery, House, HouseGallery, LandPlot, CommercialStructure, Garage


# def delete_model(modeladmin, request, queryset):
#     print('delete from admin delete_model')
#     print(modeladmin)
#     print(request)
#     print(queryset)

# Register your models here.
class ApartmentGalleryInline(admin.TabularInline):
    fk_name = 'apartment'
    model = ApartmentGallery


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    inlines = [ApartmentGalleryInline,]
    #actions = [delete_model]

    # def delete_queryset(self, request, queryset):
    #     print('========================delete_queryset========================')
    #     print(queryset)
    #     """you can do anything here BEFORE deleting the object(s)"""
    #     queryset.delete()
    #     """you can do anything here AFTER deleting the object(s)"""
    #     print('========================delete_queryset========================')
    #
    # def delete_model(self, request, obj):
    #     print('==========================delete_model==========================')
    #     print(obj)
    #     """you can do anything here BEFORE deleting the object"""
    #     obj.delete()
    #     """you can do anything here AFTER deleting the object"""
    #     print('==========================delete_model==========================')


class HouseGalleryInline(admin.TabularInline):
    fk_name = 'house'
    model = HouseGallery


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    inlines = [HouseGalleryInline,]


admin.site.register(Realtor)
admin.site.register(LandPlot)
admin.site.register(CommercialStructure)
admin.site.register(Garage)