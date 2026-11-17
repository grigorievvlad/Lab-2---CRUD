from django.db import models

MAX_LENGTH = 255


class Clienti(models.Model):
    id_client = models.AutoField(primary_key=True, db_column='ID_Client')
    fio = models.CharField(max_length=MAX_LENGTH, verbose_name='ФИО', db_column='FIO')
    adres = models.CharField(max_length=MAX_LENGTH, verbose_name='Адрес',db_column='Adres')
    telephone = models.CharField(max_length=20, verbose_name='Телефон', db_column='Telephone')
    nomer_zayavki = models.CharField(max_length=50, verbose_name='Номер заявки', db_column='Nomer_zayavki')

    def __str__(self):
        return self.fio

    class Meta:
        db_table = 'Clienti'
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class DoljnostiCotrudnikov(models.Model):
    id_dolnosti = models.AutoField(primary_key=True, db_column='ID_Dolnosti')
    doljnost = models.CharField(max_length=MAX_LENGTH, verbose_name='Должность', db_column='Doljnost')

    def __str__(self):
        return self.doljnost

    class Meta:
        db_table = 'Doljnosti_Cotrudnikov'
        verbose_name = 'Должность сотрудника'
        verbose_name_plural = 'Должности сотрудников'


class Cotrudniki(models.Model):
    id_cotrudnika = models.AutoField(primary_key=True, db_column='ID_Cotrudnika')
    lastname = models.CharField(max_length=MAX_LENGTH, verbose_name='Фамилия', db_column='Lastname')
    firstname = models.CharField(max_length=MAX_LENGTH, verbose_name='Имя', db_column='Firstname' )
    secondname = models.CharField(max_length=MAX_LENGTH,blank=True, verbose_name='Отчество', db_column='Secondname')
    number_telephone = models.CharField(max_length=20, verbose_name='Номер телефона', db_column='Number_telephone')
    address_prozhivania = models.CharField(max_length=MAX_LENGTH, verbose_name='Адрес проживания', db_column='Address_prozhivania')
    doljnost = models.ForeignKey( DoljnostiCotrudnikov, on_delete=models.PROTECT, verbose_name='Должность', db_column='ID_Dolgnosti')

    def __str__(self):
        return f'{self.lastname} {self.firstname}'

    class Meta:
        db_table = 'Cotrudniki'
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class KategoriTovarov(models.Model):
    id_category_t = models.AutoField(primary_key=True, db_column='ID_Category_T')
    category = models.CharField(max_length=MAX_LENGTH, verbose_name='Категория', db_column='Category')

    def __str__(self):
        return self.category

    class Meta:
        db_table = 'Kategori_tovarov'
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'


class Tovar(models.Model):
    id_tovara = models.AutoField(primary_key=True,db_column='ID_Tovara')
    naimenovanie = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование', db_column='Naimenovanie')
    cost = models.FloatField(verbose_name='Стоимость',db_column='Cost')
    kolichestvo_na_sklade = models.PositiveIntegerField( verbose_name='Количество на складе', db_column='Kolichestvo_na_sklade')
    category = models.ForeignKey(KategoriTovarov, on_delete=models.PROTECT,verbose_name='Категория товара', db_column='ID_Category_T')
    serial_number = models.CharField(max_length=100, verbose_name='Серийный номер', db_column='Serial_number')
    photo = models.ImageField(upload_to='image/%Y/%m/%d/', null=True, blank=True, verbose_name='Фотография товара', db_column='Photo')

    def __str__(self):
        return self.naimenovanie

    class Meta:
        db_table = 'Tovar'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class KategoriiPostavchikov(models.Model):
    id_categori_p = models.AutoField(primary_key=True, db_column='ID_Categori_P')
    category = models.CharField(max_length=MAX_LENGTH, verbose_name='Категория', db_column='Category') 

    def __str__(self):
        return self.category

    class Meta:
        db_table = 'Kategorii_postavchikov'
        verbose_name = 'Категория поставщика'
        verbose_name_plural = 'Категории поставщиков'


class Postavchik(models.Model):
    id_postavchik = models.AutoField(primary_key=True,db_column='ID_Postavchik')
    naimenovanie = models.CharField(max_length=MAX_LENGTH,verbose_name='Наименование',db_column='Naimenovanie')
    contact_telephone = models.CharField(max_length=20, verbose_name='Контактный телефон',db_column='Contact_telephone')
    adres = models.CharField(max_length=MAX_LENGTH,verbose_name='Адрес',db_column='Adres')
    nalichie_skidki = models.BooleanField(default=False, verbose_name='Наличие скидки', db_column='Nalichie_skidki')
    razmer_skidki = models.FloatField(default=0, verbose_name='Размер скидки',db_column='Razmer_skidki')
    garantia = models.CharField(max_length=MAX_LENGTH, verbose_name='Гарантия', db_column='Garantia')
    category = models.ForeignKey(KategoriiPostavchikov, on_delete=models.PROTECT, verbose_name='Категория поставщика', db_column='ID_Categori_P')
    strana = models.CharField(max_length=100, verbose_name='Страна', db_column='Strana')
    photo = models.ImageField(upload_to='image/%Y/%m/%d/', null=True, blank=True, verbose_name='Фотография поставщика', db_column='Photo')

    def __str__(self):
        return self.naimenovanie

    class Meta:
        db_table = 'Postavchik'
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Zakazi(models.Model):
    id_zakaza = models.AutoField(primary_key=True, db_column='ID_Zakaza')
    date = models.DateField(verbose_name='Дата', db_column='Date')
    kolichestvo_t = models.PositiveIntegerField(verbose_name='Количество товара', db_column='Kolichestvo_t')
    cumma = models.FloatField(verbose_name='Сумма', db_column='Cumma')
    client = models.ForeignKey(Clienti, on_delete=models.PROTECT, verbose_name='Клиент',db_column='ID_Client')
    cotrudnik = models.ForeignKey(Cotrudniki, on_delete=models.PROTECT, verbose_name='Сотрудник', db_column='ID_Cotrudnika')
    tovar = models.ForeignKey(Tovar, on_delete=models.PROTECT, verbose_name='Товар', db_column='ID_Tovara')

    def __str__(self):
        return f'Заказ №{self.id_zakaza}'

    class Meta:
        db_table = 'Zakazi'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

