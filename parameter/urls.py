from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('researches', views.ResearchViewSet)
router.register('researchers', views.ResearcherViewSet)
router.register('projects', views.ProjectViewSet)

urlpatterns = router.urls
