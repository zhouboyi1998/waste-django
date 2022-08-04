from django.urls import path, include

from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('search/<str:waste_name>', views.search)
]

router = DefaultRouter()
router.register('', views.WasteView)
urlpatterns += router.urls
