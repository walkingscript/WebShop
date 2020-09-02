from django.contrib import admin

from .models import GoodCategory, GoodType, Unit, Good, PlaceType, Contact, \
                    PhoneNumber, Email, Url, Address, GoodPlace, GoodCost, \
                    GoodCount, Employee, GoodSubjectArea, Currency


class GoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'description')
    list_display_links = ('name', 'code')
    search_fields = ('name', 'code', 'description')


class GoodTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_display_links = ('name',)
    search_fields = ('name',)


class GoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject_area')
    list_display_links = ('name',)
    search_fields = ('name',)


class UnitAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'full_name')
    list_display_links = ('short_name', 'full_name')
    search_fields = ('short_name', 'full_name')


class PlaceTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    list_display_links = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')


class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ('phone_number',)
    list_display_links = ('phone_number',)
    search_fields = ('phone_number',)


class EmailAdmin(admin.ModelAdmin):
    list_display = ('email',)
    list_display_links = ('email',)
    search_fields = ('email',)


class UrlAdmin(admin.ModelAdmin):
    list_display = ('url',)
    list_display_links = ('url',)
    search_fields = ('url',)


class AddressAdmin(admin.ModelAdmin):
    list_display = ('country', 'region', 'city', 'street',
                    'building', 'housing', 'entrance', 'floor', 'room')
    list_display_links = ('country', 'region', 'city', 'street',)
    search_fields = ('country', 'region', 'city', 'street',)


class GoodPlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'address', 'place_type')
    list_display_links = ('name',)
    search_fields = ('name', 'contact', 'address', 'place_type')


class GoodCostAdmin(admin.ModelAdmin):
    list_display = ('good', 'cost', 'currency', 'good_place')
    list_display_links = ('cost',)
    search_fields = ('cost',)


class GoodCountAdmin(admin.ModelAdmin):
    list_display = ('good', 'count', 'good_place',)
    list_display_links = ('good', 'count', 'good_place',)
    search_fields = ('good', 'count', 'good_place',)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('contact', 'position_name', 'job_place', 'address')
    list_display_links = ('contact', 'position_name', 'job_place', 'address')
    search_fields = ('contact', 'position_name', 'job_place', 'address')


class GoodSubjectAreaAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name')
    list_display_links = ('name', 'short_name')
    search_fields = ('name', 'short_name')


admin.site.register(GoodCategory, GoodCategoryAdmin)
admin.site.register(GoodType, GoodTypeAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Good, GoodAdmin)
admin.site.register(PlaceType, PlaceTypeAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(PhoneNumber, PhoneNumberAdmin)
admin.site.register(Email, EmailAdmin)
admin.site.register(Url, UrlAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(GoodPlace, GoodPlaceAdmin)
admin.site.register(GoodCost, GoodCostAdmin)
admin.site.register(GoodCount, GoodCountAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(GoodSubjectArea, GoodSubjectAreaAdmin)
admin.site.register(Currency, CurrencyAdmin)
