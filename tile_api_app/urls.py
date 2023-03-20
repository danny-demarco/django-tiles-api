from django.urls import include, path
from . import views

router = views.router

urlpatterns = [
    path('', include(router.urls)),
]