from django.contrib import admin
from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
# admin.autodiscover()
# admin.site.enable_nav_sidebar = False

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('basics.urls'))
]

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
