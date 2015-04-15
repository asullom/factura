from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers

from cartera.views import ClienteViewSet

router = routers.DefaultRouter()
router.register(r'clientes', ClienteViewSet)


urlpatterns = [
    # Examples:
    # url(r'^$', 'factura.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include(router.urls)),

    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework'))
]
