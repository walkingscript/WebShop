from django.contrib import admin

from .models import GoodCategory, GoodType, Unit, Good, PlaceType, Contact, \
                    PhoneNumber, Email, Url, Address, GoodPlace, GoodCost, \
                    GoodCount, Employee, GoodSubjectArea

admin.site.register(GoodCategory)
admin.site.register(GoodType)
admin.site.register(Unit)
admin.site.register(Good)
admin.site.register(PlaceType)
admin.site.register(Contact)
admin.site.register(PhoneNumber)
admin.site.register(Email)
admin.site.register(Url)
admin.site.register(Address)
admin.site.register(GoodPlace)
admin.site.register(GoodCost)
admin.site.register(GoodCount)
admin.site.register(Employee)
admin.site.register(GoodSubjectArea)
