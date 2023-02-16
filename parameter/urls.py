from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('person', views.PersonViewSet)
router.register('researches', views.ResearchViewSet)
router.register('researchers', views.ResearcherViewSet)
router.register('projects', views.ProjectViewSet)
router.register('salog_employees', views.SALOG_EmployeeViewSet)

urlpatterns = router.urls
