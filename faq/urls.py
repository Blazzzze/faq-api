from django.urls import path, include
from rest_framework.routers import DefaultRouter
from faq.views import FAQViewSet
from django.contrib import admin

router = DefaultRouter()
router.register(r"faqs", FAQViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
