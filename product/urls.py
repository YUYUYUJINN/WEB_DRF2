from rest_framework.routers import DefaultRouter
from django.urls import path, include
import product.views

router = DefaultRouter()
router.register('product', product.views.ProductViewSet)
urlpatterns = [
    path('', include(router.urls)),
]