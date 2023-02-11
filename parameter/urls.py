from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('researches', views.ResearchViewSet)

urlpatterns = router.urls
