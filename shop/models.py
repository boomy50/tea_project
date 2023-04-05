from django.db import models
from django.urls import reverse


# Slug - это часть URL, которая идентифицирует конкретную страницу на сайте в форме, доступной для чтения пользователями
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                        args=[self.slug])


class Roles(models.Model):
    title = models.CharField(max_length = 20)



class Users(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role_id = models.ForeignKey(Roles, on_delete=models.DO_NOTHING)



class Statuses(models.Model):
    title = models.CharField(max_length = 20)



class Orders(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    total_price = models.SmallIntegerField()
    date = models.DateField()
    phone_number = models.CharField(max_length=25)
    status_id = models.ForeignKey(Statuses, on_delete=models.DO_NOTHING)



class Products(models.Model):
    category = models.ForeignKey(Category, related_name='products', null=True, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length = 200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, null=True)
    #image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.SmallIntegerField()
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('title',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return f'{self.title}: Кол-во на складе - {self.stock}'

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                        args=[self.id, self.slug])

class Order_products(models.Model):
    order_id = models.ForeignKey(Orders, on_delete=models.DO_NOTHING)
    product_id = models.ForeignKey(Products, on_delete=models.DO_NOTHING)