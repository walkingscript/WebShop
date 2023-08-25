from django.db import models


class GoodSubjectArea(models.Model):
    """Subject area which includes a good."""
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'предметные области товаров'
        verbose_name = 'предметная область товара'


class GoodCategory(models.Model):
    """Categories where goods can be related to."""
    subject_area = models.ForeignKey(GoodSubjectArea, verbose_name='предметная область', on_delete=models.PROTECT,
                                     null=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}; Предметная область: {self.subject_area.name}'

    class Meta:
        verbose_name_plural = 'категории товаров'
        verbose_name = 'категория товара'


class GoodType(models.Model):
    """Types of goods related to the categories."""
    category = models.ForeignKey(GoodCategory, on_delete=models.PROTECT, null=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}; Категория: {self.category}'

    class Meta:
        verbose_name_plural = 'типы товаров'
        verbose_name = 'тип товара'


class Unit(models.Model):
    """Units which goods can be counted in."""
    full_name = models.CharField(max_length=20)
    short_name = models.CharField(max_length=5)

    def __str__(self):
        return self.short_name

    class Meta:
        verbose_name_plural = 'единицы измерения'
        verbose_name = 'единица измерения'


class Good(models.Model):
    """Goods which the shop can sell in."""
    type = models.ForeignKey(GoodType, verbose_name='тип', on_delete=models.PROTECT, null=True)
    unit = models.ForeignKey(Unit, verbose_name='единица измерения', on_delete=models.PROTECT, null=True)
    name = models.CharField(max_length=300, verbose_name='наименовние')
    code = models.CharField(max_length=50, verbose_name='код')
    description = models.TextField(verbose_name='описание товара', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'товары'
        verbose_name = 'товар'


class PlaceType(models.Model):
    """Types of good's location.
    Examples: warehouse, shop, pickup point"""
    name = models.CharField(max_length=30, verbose_name='наименование типа')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'типы мест размещения товаров'
        verbose_name = 'тип места размещения товара'


class Contact(models.Model):
    """Contact data of employees, clients and so on."""
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    passport = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ' \
               f'{f", паспорт {str(self.passport).upper()}" if self.passport else ""}'

    class Meta:
        verbose_name_plural = 'контакты'
        verbose_name = 'контакт'


class PhoneNumber(models.Model):
    """Phone numbers of employees, clients and so on."""
    contact = models.ForeignKey(Contact, verbose_name='контакт', on_delete=models.PROTECT, null=True)
    phone_number = models.CharField(max_length=30, verbose_name='номер телефона')

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name_plural = 'номера телефонов'
        verbose_name = 'номер телефона'


class Email(models.Model):
    """Addresses of employees, clients and so on."""
    contact = models.ForeignKey(Contact, verbose_name='контакт', on_delete=models.PROTECT, null=True)
    email = models.CharField(max_length=100, verbose_name='электронная почта')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'адреса электронной почты'
        verbose_name = 'адрес электронной почты'


class Url(models.Model):
    """URLs of different sources related to employees, clients and so on."""
    contact = models.ForeignKey(Contact, verbose_name='контакт', on_delete=models.PROTECT, null=True)
    url = models.TextField(verbose_name='ссылка')

    def __str__(self):
        return self.url

    class Meta:
        verbose_name_plural = 'ссылки'
        verbose_name = 'ссылка'


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
        verbose_name_plural = 'адреса'
        verbose_name = 'адрес'


class GoodPlace(models.Model):
    """Места расположения товаров."""
    place_type = models.ForeignKey(PlaceType, verbose_name='тип места', on_delete=models.PROTECT, null=True)
    address = models.ForeignKey(Address, verbose_name='адрес', on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, verbose_name='контакт', on_delete=models.CASCADE)
    name = models.CharField(max_length=300, verbose_name='название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'места расположения товаров'
        verbose_name = 'место расположения товара'


class Currency(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование валюты')
    short_name = models.CharField(max_length=3, verbose_name='код')

    def __str__(self):
        return f'{self.short_name} - {self.name}'

    class Meta:
        verbose_name_plural = 'валюты'
        verbose_name = 'валюта'


class GoodCost(models.Model):
    """Сведения о ценах на товар в разных магазинах."""
    good_place = models.ForeignKey(GoodPlace, verbose_name='месторасположение товара', on_delete=models.PROTECT,
                                   null=True)
    good = models.ForeignKey(Good, verbose_name='товар', on_delete=models.PROTECT, null=True)
    currency = models.ForeignKey(Currency, verbose_name='валюта', on_delete=models.PROTECT, null=True)
    cost = models.FloatField(verbose_name='цена товара')

    def __str__(self):
        return f'{self.good_place}\n{self.good.name}\nСтоимость: {self.cost}'

    class Meta:
        verbose_name_plural = 'цены на товары'
        verbose_name = 'цена товара'


class GoodCount(models.Model):
    """Количество каждого наименования товара в каждом магазине."""
    good_place = models.ForeignKey(GoodPlace, verbose_name='местонахождение', on_delete=models.PROTECT, null=True)
    good = models.ForeignKey(Good, verbose_name='товар', on_delete=models.PROTECT, null=True)
    count = models.FloatField(default=0.0, verbose_name='количество')

    def __str__(self):
        return f'{self.good_place.name}\n{self.good.name}\nКоличество: {self.count}'

    class Meta:
        verbose_name_plural = 'количество товаров'
        verbose_name = 'количество товара'


class Employee(models.Model):
    """Сотрудники магазинов."""
    contact = models.ForeignKey(Contact, verbose_name='контакт сотрудника', on_delete=models.CASCADE)
    address = models.ForeignKey(Address, verbose_name='адрес сотрудника', on_delete=models.CASCADE)
    job_place = models.ForeignKey(GoodPlace, verbose_name='место работы', on_delete=models.PROTECT, null=True)
    position_name = models.CharField(max_length=50, verbose_name='должность')

    def __str__(self):
        return self.position_name

    class Meta:
        verbose_name_plural = 'сотрудники магазинов'
        verbose_name = 'сотрудник магазина'
