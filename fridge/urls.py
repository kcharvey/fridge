from django.conf.urls import patterns, include, url

from rest_framework import routers

from food import views


router = routers.DefaultRouter()
router.register(r'food', views.FoodViewSet)
router.register(r'recipes', views.RecipeViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', 
        include('rest_framework.urls', namespace='rest_framework')
    ),
)
