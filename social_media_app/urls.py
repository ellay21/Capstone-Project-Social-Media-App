from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

def home(request):
    return HttpResponse("Successfully Worked!")

schema_view = get_schema_view(
    openapi.Info(
        title="Social Media App API",
        default_version='v1',
        description="API documentation for the Social Media App",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="henokdagen19@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/', include('posts.urls')),
    # swagger and redoc urls
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
