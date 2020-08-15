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
    subject_area = models.ForeignKey(GoodSubjectArea,
                                     verbose_name='предметная область',
                                     on_delete=models.DO_NOTHING,
                                     null=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}; Предметная область: {self.subject_area.name}'

    class Meta:
        verbose_name_plural = 'goods categories'


class GoodType(models.Model):
    """Типы товаров, относящиеся к категориям"""
    category = models.ForeignKey(GoodCategory, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}; Категория: {self.category}'

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
    type = models.ForeignKey(GoodType, verbose_name='тип',
                             on_delete=models.DO_NOTHING)
    unit = models.ForeignKey(Unit, verbose_name='единица измерения',
                             on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=300, verbose_name='наименовние')
    code = models.CharField(max_length=50, verbose_name='код')
    description = models.TextField(verbose_name='описание товара', null=True)
    cost = models.FloatField(verbose_name='цена')

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
    passport = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ' \
               f'{f", паспорт {str(self.passport).upper()}" if self.passport else ""}'


class PhoneNumber(models.Model):
    """Номера телефонов сотрудников, клиентов, и др."""
    contact = models.ForeignKey(Contact, on_delete=models.DO_NOTHING,
                                verbose_name='контакт')
    phone_number = models.CharField(max_length=30, verbose_name='номер телефона')

    def __str__(self):
        return self.phone_number


class Email(models.Model):
    """Адреса электронной почты сотрудников, клиентов и др."""
    contact = models.ForeignKey(Contact, on_delete=models.DO_NOTHING,
                                verbose_name='контакт')
    email = models.CharField(max_length=100, verbose_name='электронная почта')

    def __str__(self):
        return self.email


class Url(models.Model):
    """Ссылки на различные ресурсы, относящиеся к сотрудникам, клиентам и др."""
    contact = models.ForeignKey(Contact, on_delete=models.DO_NOTHING,
                                verbose_name='контакт')
    url = models.TextField(verbose_name='ссылка')

    def __str__(self):
        return self.url


class Address(models.Model):
    """Адреса сотрудников, клиентов и др."""
    country = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=50)
    building = models.IntegerField()
    housing = models.IntegerField(null=True)
    entrance = models.IntegerField(null=True)
    floor = models.IntegerField(null=True)
    room = models.IntegerField(null=True)

    def __str__(self):
        return f'{f"Страна {self.country}," if self.country else ""}' \
               f'{f"{self.region} обл.," if self.country else ""}' \
               f'{f"г. {self.city}," if self.city else ""}' \
               f'{f"ул. {self.street}," if self.street else ""}' \
               f'{f"здание {self.building}," if self.building else ""}' \
               f'{f"корпус {self.housing}," if self.housing else ""}' \
               f'{f"подъезд {self.entrance}," if self.entrance else ""}' \
               f'{f"этаж {self.floor}," if self.floor else ""}' \
               f'{f"помещение {self.room}" if self.room else ""}'

    class Meta:
        verbose_name_plural = 'addresses'


class GoodPlace(models.Model):
    """Места расположения товаров."""
    place_type = models.ForeignKey(PlaceType, verbose_name='тип места',
                                   on_delete=models.DO_NOTHING)
    address = models.ForeignKey(Address, verbose_name='адрес',
                                on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, verbose_name='контакт',
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=300, verbose_name='название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'goods place'


class GoodCost(models.Model):
    """Сведения о ценах на товар в разных магазинах."""
    good_place = models.ForeignKey(GoodPlace,
                                   verbose_name='месторасположение товара',
                                   on_delete=models.DO_NOTHING)
    good = models.ForeignKey(Good, verbose_name='товар',
                             on_delete=models.DO_NOTHING)
    cost = models.FloatField(verbose_name='цена товара')

    def __str__(self):
        return f'{self.good_place}\n{self.good.name}\nСтоимость: {self.cost}'

    class Meta:
        verbose_name_plural = 'goods cost'


class GoodCount(models.Model):
    """Количество каждого наименования товара в каждом магазине."""
    good_place = models.ForeignKey(GoodPlace, verbose_name='местонахождение',
                                   on_delete=models.DO_NOTHING)
    good = models.ForeignKey(Good, verbose_name='товар',
                             on_delete=models.DO_NOTHING)
    count = models.FloatField(default=0.0, verbose_name='количество')

    def __str__(self):
        return f'{self.good_place.name}\n{self.good.name}\nКоличество: {self.count}'

    class Meta:
        verbose_name_plural = 'goods count'


class Employee(models.Model):
    """Сотрудники магазинов."""
    contact = models.ForeignKey(Contact, verbose_name='контакт сотрудника',
                                on_delete=models.CASCADE)
    address = models.ForeignKey(Address, verbose_name='адрес сотрудника',
                                on_delete=models.CASCADE)
    job_place = models.ForeignKey(GoodPlace, verbose_name='место работы',
                                  on_delete=models.DO_NOTHING)
    position_name = models.CharField(max_length=50, verbose_name='должность')

    def __str__(self):
        return self.position_name
