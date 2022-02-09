from django.db import models

# Create your models here.


class CategoryProcedure(models.Model):
    en_title = models.CharField(max_length=255, verbose_name="Titel (DEU)")
    de_title = models.CharField(max_length=255, verbose_name="Title (ENG)")
    ru_title = models.CharField(max_length=255, verbose_name="Название (RUS)")
    icon = models.ImageField(upload_to='icons', verbose_name="Icon")
    def __str__(self):
        return self.en_title

    class Meta:
        verbose_name = "Категория процедуры"
        verbose_name_plural = "Категории процедур"
        managed = False
        db_table = 'tbl_category_procedures'

class Procedure(models.Model):
    sexs = (
        ('F', 'Female'),
        ('M', 'Male'),
    )
    category = models.ForeignKey('CategoryProcedure',verbose_name="Category",null="True", on_delete=models.PROTECT)
    en_title = models.CharField(max_length=255, verbose_name="Titel (DEU)")
    de_title = models.CharField(max_length=255, verbose_name="Title (ENG)")
    ru_title = models.CharField(max_length=255, verbose_name="Название (RUS)")
    price = models.FloatField(verbose_name="Price €")
    sex = models.CharField( max_length=255,choices=sexs,default="Male",verbose_name="Sex")

    def __str__(self):
        return self.en_title
    class Meta:
        verbose_name = "Процедура"
        verbose_name_plural = "Процедуры"
        managed = False
        db_table = 'tbl_procedures'