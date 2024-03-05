from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    # Дополнительные поля можно добавить здесь
    pass

    def __str__(self):
        return self.username


class Brand(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Model(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='название продукта')
    description = models.TextField(verbose_name='описание')
    color = models.CharField(max_length=50)
    screen_size = models.CharField(max_length=32, verbose_name='размер экрана')
    screen_technology = models.CharField(max_length=50,
                                         verbose_name='технология, используемая на экране (например, OLED)')
    processor = models.CharField(max_length=50, verbose_name='процессор')
    rom = models.IntegerField()
    ram = models.IntegerField(verbose_name="количество ядер")
    camera_resolution = models.CharField(max_length=50)
    video_resolution = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    warranty = models.IntegerField()

    def __str__(self):
        return self.name


class ProductPhoto(models.Model):
    photo = models.ImageField(upload_to="images/", blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Favorite(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user_id


class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.user_id


class Color(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)  # Например, можно использовать шестнадцатеричное значение цвета

    def __str__(self):
        return self.name or self.code

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"


class Rating(models.Model):
    """Рейтинг"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="продукт")
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)],
                                help_text="Rate the item with 0 to 6 stars.", verbose_name="Rating")

    def __str__(self):
        return f"{self.product} - {self.user} - {self.stars} stars"


    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"



class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, default=1, related_name='product_favorite')
    summ_products = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user} - {self.product}'


class Reviews(models.Model):
    """Отзывы"""
    author = models.ForeignKey(User, models.CASCADE)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    product = models.ForeignKey(Product, verbose_name="фильм", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.product}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

