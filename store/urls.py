from rest_framework.routers import DefaultRouter
from pprint import pprint
from store import views

router = DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)
pprint(router.urls)
urlpatterns = router.urls

