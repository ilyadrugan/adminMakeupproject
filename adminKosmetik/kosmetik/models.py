from django.db import models

# Create your models here.


class CategoryProcedure(models.Model):
    de_title = models.CharField(max_length=255, verbose_name="Titel (DEU)")
    en_title = models.CharField(max_length=255, verbose_name="Title (ENG)")
    ru_title = models.CharField(max_length=255, verbose_name="Название (RUS)")
    icon = models.ImageField(upload_to='icons', verbose_name="Icon")
    picture = models.ImageField(upload_to='category_pictures', verbose_name="Picture")
    def __str__(self):
        return self.en_title

    class Meta:
        verbose_name = "Категория процедуры"
        verbose_name_plural = "Категории процедур"
        managed = False
        db_table = 'tbl_category_procedures'

class Procedure(models.Model):
    category = models.ForeignKey('CategoryProcedure',verbose_name="Category",null="True", on_delete=models.PROTECT)
    de_title = models.CharField(max_length=255, verbose_name="Titel (DEU)")
    en_title = models.CharField(max_length=255, verbose_name="Title (ENG)")
    ru_title = models.CharField(max_length=255, verbose_name="Название (RUS)")
    price_women = models.FloatField(verbose_name="Price for women €")
    price_men = models.FloatField(verbose_name="Price for men €")

    def __str__(self):
        return self.en_title
    class Meta:
        verbose_name = "Процедура"
        verbose_name_plural = "Процедуры"
        managed = False
        db_table = 'tbl_procedures'

class Contacts(models.Model):
    phone_number = models.CharField(max_length=255, verbose_name="Phone")
    map_position = models.CharField(max_length=255, verbose_name="Address")
    email = models.CharField(max_length=255, verbose_name="E-mail")
    site = models.CharField(max_length=255, verbose_name="Site")
    facebook_link = models.CharField(max_length=255, verbose_name="Facebook")
    instagram_link = models.CharField(max_length=255, verbose_name="Instagram")

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        managed = False
        db_table = 'tbl_contacts'

class Requests(models.Model):
    category_name = models.CharField(max_length=255, verbose_name="Category")
    procedure_name = models.CharField(max_length=255, verbose_name="Procedure")
    sex = models.CharField(max_length=255, verbose_name="Sex")
    price = models.CharField(max_length=255, verbose_name="Price")
    first_name = models.CharField(max_length=255, verbose_name="First name")
    last_name = models.CharField(max_length=255, verbose_name="Last name")
    email = models.CharField(max_length=255, verbose_name="Email")
    phone = models.CharField(max_length=255, verbose_name="Phone")
    time = models.CharField(max_length=255, verbose_name="Time")
    time_create = models.DateTimeField(auto_now_add=True,  verbose_name="Time created")

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
        managed = False
        db_table = 'tbl_requests'