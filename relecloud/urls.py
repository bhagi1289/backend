#App (Relecloud)

from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register(r'destinations', views.DestinationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # Add 'api/' prefix here
]