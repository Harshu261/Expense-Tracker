from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from sales.views import PlateSaleViewSet,RawItemViewSet,MainItemViewSet

router = DefaultRouter()

router.register(r'plates',PlateSaleViewSet)
router.register(r'raw',RawItemViewSet)
router.register(r'main',MainItemViewSet)
urlpatterns = [
    path('',include(router.urls)),
]
