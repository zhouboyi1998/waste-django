from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = []

router = DefaultRouter()
router.register('', views.CategoryView)
urlpatterns += router.urls
