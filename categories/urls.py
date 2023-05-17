from django.urls import include
from django.urls import path

from .routers import router

urlpatterns = []
urlpatterns += router.urls
