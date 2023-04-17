"""glubble_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.urls import include, path
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.utils.translation import gettext
from django.shortcuts import redirect
# from django.conf.urls import urlpatterns
from django.contrib.sitemaps import GenericSitemap # new
from django.contrib.sitemaps.views import sitemap # new
from django.contrib.sitemaps.views import sitemap

from core.models import GPUSpecs # new
from core.sitemaps import GPUSpecsSitemap,StaticSitemap,CompareGPUSpecsSitemap

info_dict = {
    'queryset': GPUSpecs.objects.all(),
}

sitemaps = {
    'GPUSpecs':GPUSpecsSitemap,
    'compare_gpus': CompareGPUSpecsSitemap,
    # 'static':StaticSitemap #add StaticSitemap to the dictionary
}

urlpatterns = []

urlpatterns += i18n_patterns(
    path('', lambda req: redirect('/graphics-cards')),
    path('', include('frontend.urls')),
    path(_("admin/"), admin.site.urls, name="admin"),
)

# urlpatterns = [
#     path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
# ]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
