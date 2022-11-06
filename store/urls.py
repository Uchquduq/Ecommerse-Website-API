from rest_framework_nested import routers
from store import views

router = routers.DefaultRouter()
router.register("products", views.ProductViewSet, basename='products')
router.register("collections", views.CollectionViewSet, basename="collections")
router.register('carts', views.CartViewSet, basename="carts")


products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')

products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')


# URL Conf

urlpatterns = router.urls + products_router.urls
