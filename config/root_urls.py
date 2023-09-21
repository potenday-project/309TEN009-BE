from rest_framework import permissions

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="으쌰!",
        default_version="v1",
        description="으쌰! API",
        terms_of_service="https://www.ourapp.com/policies/terms/",
        contact=openapi.Contact(email="wogur981208@gmail.com"),
        license=openapi.License(name="euss-ya! License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),
    # API V1
    path("api/v1/users/", include("euss_ya.users.urls")),
    path("api/v1/exercises/", include("euss_ya.exercises.urls")),
    # Swagger
    path("swagger/docs", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("swagger/redoc", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

# Static/Media File Root (CSS, JavaScript, Images)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
