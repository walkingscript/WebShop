from django.db import models


class GoodSubjectArea(models.Model):
    """Предметная область, в которой находится товар."""
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'goods subject area'


class GoodCategory(models.Model):
    """Категории, к которым могут относиться товары"""
    subject_area_set = models.ForeignKey(GoodSubjectArea,
                                         verbose_name='предметная область',
                                         on_delete=models.DO_NOTHING,
                                         null=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}; Предметная область: {self.subject_area_set.name}'

    class Meta:
        verbose_name_plural = 'goods categories'


class GoodType(models.Model):
    """Типы товаров, относящиеся к категориям"""
    category_set = models.ForeignKey(GoodCategory, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}; Категория: {self.category_set}'

    class Meta:
        verbose_name_plural = 'goods types'


class Unit(models.Model):
    """Единицы измерения, в которых может исчисляться товар"""
    full_name = models.CharField(max_length=20)
    short_name = models.CharField(max_length=5)

    def __str__(self):
        return self.short_name


class Good(models.Model):
    """Товары, которые могут продаваться в магазине"""
    type_set = models.ForeignKey(GoodType, verbose_name='тип',
                                 on_delete=models.DO_NOTHING)
    unit_set = models.ForeignKey(Unit, verbose_name='единица измерения',
                                 on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=300, verbose_name='наименовние')
    code = models.CharField(max_length=50, verbose_name='код')
    description = models.TextField(verbose_name='описание товара', null=True)

    def __str__(self):
        return self.name


class PlaceType(models.Model):
    """Тип места размещения товара.
    Примеры: склад, магазин, пункт самовывоза"""
    name = models.CharField(max_length=30, verbose_name='наименование типа')

    def __str__(self):
        return self.name


class Contact(models.Model):
    """Контактные данные сотрудников, клиентов и др."""
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    passport = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ' \
               f'{f", паспорт {str(self.passport).upper()}" if self.passport else ""}'


class PhoneNumber(models.Model):
    """Номера телефонов сотрудников, клиентов, и др."""
    contact_set = models.ForeignKey(Contact, verbose_name='контакт',
                                    on_delete=models.DO_NOTHING)
    phone_number = models.CharField(max_length=30, verbose_name='номер телефона')

    def __str__(self):
        return self.phone_number


class Email(models.Model):
    """Адреса электронной почты сотрудников, клиентов и др."""
    contact_set = models.ForeignKey(Contact, verbose_name='контакт',
                                    on_delete=models.DO_NOTHING)
    email = models.CharField(max_length=100, verbose_name='электронная почта')

    def __str__(self):
        return self.email


class Url(models.Model):
    """Ссылки на различные ресурсы, относящиеся к сотрудникам, клиентам и др."""
    contact_set = models.ForeignKey(Contact, verbose_name='контакт',
                                    on_delete=models.DO_NOTHING)
    url = models.TextField(verbose_name='ссылка')

    def __str__(self):
        return self.url


class Address(models.Model):
    """Адреса сотрудников, клиентов, мест и др."""
    country = models.CharField(max_length=30, verbose_name='страна')
    region = models.CharField(max_length=30, verbose_name='область')
    city = models.CharField(max_length=30, verbose_name='город')
    street = models.CharField(max_length=50, verbose_name='улица')
    building = models.IntegerField(verbose_name='номер здания')
    housing = models.IntegerField(blank=True, verbose_name='корпус', null=True)
    entrance = models.IntegerField(blank=True, verbose_name='подъезд', null=True)
    floor = models.IntegerField(blank=True, verbose_name='этаж', null=True)
    room = models.IntegerField(blank=True, verbose_name='помещение', null=True)

    def __str__(self):
        return f'{f"{self.country}" if self.country else ""}' \
               f'{f", {self.region} обл." if self.country else ""}' \
               f'{f", г. {self.city}" if self.city else ""}' \
               f'{f", ул. {self.street}" if self.street else ""}' \
               f'{f", {self.building}" if self.building else ""}' \
               f'{f", корпус {self.housing}" if self.housing else ""}' \
               f'{f", подъезд {self.entrance}" if self.entrance else ""}' \
               f'{f", этаж {self.floor}" if self.floor else ""}' \
               f'{f", пом. {self.room}" if self.room else ""}'

    class Meta:
        verbose_name_plural = 'addresses'


class GoodPlace(models.Model):
    """Места расположения товаров."""
    place_type_set = models.ForeignKey(PlaceType, verbose_name='тип места',
                                       on_delete=models.DO_NOTHING)
    address_set = models.ForeignKey(Address, verbose_name='адрес',
                                    on_delete=models.CASCADE)
    contact_set = models.ForeignKey(Contact, verbose_name='контакт',
                                    on_delete=models.CASCADE)
    name = models.CharField(max_length=300, verbose_name='название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'goods place'


class Currency(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование валюты')
    short_name = models.CharField(max_length=3, verbose_name='код')

    def __str__(self):
        return f'{self.short_name} - {self.name}'

    class Meta:
        verbose_name_plural = 'currency'


class GoodCost(models.Model):
    """Сведения о ценах на товар в разных магазинах."""
    good_place_set = models.ForeignKey(GoodPlace,
                                       verbose_name='месторасположение товара',
                                       on_delete=models.DO_NOTHING)
    good_set = models.ForeignKey(Good, verbose_name='товар',
                                 on_delete=models.DO_NOTHING)
    currency_set = models.ForeignKey(Currency, verbose_name='валюта',
                                     on_delete=models.DO_NOTHING,
                                     null=True)
    cost = models.FloatField(verbose_name='цена товара')

    def __str__(self):
        return f'{self.good_place_set}\n{self.good_set.name}\nСтоимость: {self.cost}'

    class Meta:
        verbose_name_plural = 'goods cost'


class GoodCount(models.Model):
    """Количество каждого наименования товара в каждом магазине."""
    good_place_set = models.ForeignKey(GoodPlace, verbose_name='местонахождение',
                                       on_delete=models.DO_NOTHING)
    good_set = models.ForeignKey(Good, verbose_name='товар',
                                 on_delete=models.DO_NOTHING)
    count = models.FloatField(default=0.0, verbose_name='количество')

    def __str__(self):
        return f'{self.good_place_set.name}\n{self.good_set.name}\nКоличество: {self.count}'

    class Meta:
        verbose_name_plural = 'goods count'


class Employee(models.Model):
    """Сотрудники магазинов."""
    contact_set = models.ForeignKey(Contact, verbose_name='контакт сотрудника',
                                    on_delete=models.CASCADE)
    address_set = models.ForeignKey(Address, verbose_name='адрес сотрудника',
                                    on_delete=models.CASCADE)
    job_place_set = models.ForeignKey(GoodPlace, verbose_name='место работы',
                                      on_delete=models.DO_NOTHING)
    position_name = models.CharField(max_length=50, verbose_name='должность')

    def __str__(self):
        return self.position_name
