from django.urls import include, path
from rest_framework import routers

from .views import (
    FollowViewSet,
    IngredientViewSet,
    RecipeViewSet,
)


router = routers.DefaultRouter()
router.register(r'ingredients', IngredientViewSet)
router.register(r'recipes', RecipeViewSet)
router.register(r'users', FollowViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
