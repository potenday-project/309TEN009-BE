from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/exercise', include('euss_ya_apps.exercises.urls')),
    path('api/v1/exercise', include('euss_ya_apps.users.urls')),
]

urlpatterns = []