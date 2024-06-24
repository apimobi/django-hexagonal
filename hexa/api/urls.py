from django.urls import include, path
from .views import OfferListApiView, OfferDetailApiView

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('offers/<int:offer_id>', OfferDetailApiView.as_view()),
    path('offers', OfferListApiView.as_view()),
]