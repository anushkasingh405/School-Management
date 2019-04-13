from django.urls import path
from rest_framework import routers
from .api import loginViewSet
from django.urls import include
from django.conf.urls import url
router=routers.DefaultRouter()
router.register('api/login',loginViewSet,'login')
urlpatterns=router.urls
url('^api-auth/', include('rest_framework.urls'))



