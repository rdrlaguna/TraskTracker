from django.urls import include, path
from .views import MyView, CategoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'category', CategoryViewSet, basename='category')


urlpatterns = [
    path('hello/', MyView.as_view(), name="hello"),
    path('', include(router.urls)),
]

