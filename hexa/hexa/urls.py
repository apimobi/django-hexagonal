from django.urls import include, path
from django.contrib import admin
from api import urls as api_urls

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(api_urls))
]