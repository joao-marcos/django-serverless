from django.urls import include, path
from rest_framework.routers import DefaultRouter

from books import views

router = DefaultRouter(trailing_slash=False)
router.register(r'books', views.BookViewset)

urlpatterns = [
    path("", include(router.urls)),
]