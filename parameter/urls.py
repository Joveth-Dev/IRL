from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('persons', views.PersonViewSet)
router.register('coordinators', views.CoordinatorViewSet)
router.register('programs', views.ProgramViewSet)
router.register('SALOG_employees', views.SALOG_EmployeeViewSet)
router.register('projects', views.ProjectViewSet)
router.register('researchers', views.ResearcherViewSet)
router.register('researches', views.ResearchViewSet)
router.register('equipments', views.EquipmentViewSet)
router.register('linkage_partners', views.LinkagePartnerViewSet)

urlpatterns = router.urls
