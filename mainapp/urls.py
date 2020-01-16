
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from mainapp import views

router = DefaultRouter()
router.register(r'notes', views.NoteViewSet)
router.register(r'dbitem', views.DBItemViewSet)


urlpatterns = [
	path('', include(router.urls))
]