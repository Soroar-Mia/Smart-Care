from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('list', views.DoctorViewset)
router.register('designation', views.DesignationViewset)
router.register('available_time', views.AvailableTimeViewset)
router.register('Review', views.ReviewViewset)
router.register('Specialization', views.SpecializationViewset)

urlpatterns = [
    path('', include(router.urls)),
]