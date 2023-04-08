from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('activities', views.ActivityViewSet)
router.register('news', views.NewsViewSet)

urlpatterns = router.urls
