from django.urls import include, path
from django.conf import settings
from rest_framework import routers, serializers, viewsets
from order_rest import views


router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'order', views.OrderViewSet)
router.register(r'customer', views.CustomerViewSet)
router.register(r'table', views.TableViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
