from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя категории')
    sluf = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.CASCADE
    )
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', null=True)
    price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        verbose_name='Цена'
    )

    def __str__(self):
        return self.title


class CartProduct(models.Model):
    user = models.ForeignKey(
        'Customer',
        verbose_name='Пользователь',
        on_delete=models.CASCADE
    )
    cart = models.ForeignKey(
        'Cart',
        verbose_name='Корзина',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        verbose_name='Товар',
        on_delete=models.CASCADE
    )