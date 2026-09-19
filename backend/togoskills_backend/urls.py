from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import SkillViewSet, JobViewSet, recommend_jobs

router = DefaultRouter()
router.register(r'skills', SkillViewSet)
router.register(r'jobs', JobViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/recommend/', recommend_jobs),
]