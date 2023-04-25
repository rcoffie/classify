"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", include("admin_honeypot.urls", namespace="admin_honeypot")),
    path("classify/", admin.site.urls),
    path("", include("pages.urls")),
    path("item_engine/", include("item_engine.urls")),
    path("user_engine/", include("user_engine.urls")),
    path("inbox/", include("conversation.urls")),
    path('item_engine_api/', include("item_engine_api.urls")),
    path('pages_api/', include("pages_api.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
