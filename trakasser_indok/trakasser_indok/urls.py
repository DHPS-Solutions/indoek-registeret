from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from indoker import views as indoker_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('indoker/', include('indoker.urls')),
    path('', indoker_views.indoker_list, name="home"),
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + staticfiles_urlpatterns()
