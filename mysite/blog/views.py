from rest_framework import viewsets
from .models import *
from .serializers import *


class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()  # Должно быть User.objects.all() вместо просто User
    serializer_class = UserSerializer


class CategoryViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all()  # Аналогично
    serializer_class = CategorySerializer


class ProductViewSets(viewsets.ModelViewSet):
    queryset = Product.objects.all()  # Аналогично
    serializer_class = ProductSerializer


class ReviewViewSets(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()  # Исправление имени модели Review
    serializer_class = ReviewSerializer


class RatingViewSets(viewsets.ModelViewSet):
    queryset = Rating.objects.all()  # Аналогично
    serializer_class = RatingSerializer


class FavoriteViewSets(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()  # Аналогично
    serializer_class = FavoriteSerializer


class BasketViewSets(viewsets.ModelViewSet):
    queryset = Basket.objects.all()  # Аналогично
    serializer_class = BasketSerializer


class ProductPhotoViewSets(viewsets.ModelViewSet):
    queryset = ProductPhoto.objects.all()  # Аналогично
    serializer_class = ProductPhotoSerializer


class BrandViewSets(viewsets.ModelViewSet):
    queryset = Brand.objects.all()  # Аналогично
    serializer_class = BrandSerializer


class OrderViewSets(viewsets.ModelViewSet):
    queryset = Order.objects.all()  # Аналогично
    serializer_class = OrderSerializer


class ModelViewSets(viewsets.ModelViewSet):
    queryset = Model.objects.all()  # Исправление имени модели Model
    serializer_class = ModelSerializer


class ColorViewSets(viewsets.ModelViewSet):
    queryset = Color.objects.all()  # Аналоги чно
    serializer_class = ColorSerializer
