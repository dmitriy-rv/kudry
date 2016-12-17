"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls.static import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings


from django.conf.urls import url, include
from django.contrib import admin
from hotel.views import main, action, rooms, about, reviews, service, one_service, send_review, admin_service, admin_take_data, admin_manage_number, admin_manage_tenant

urlpatterns = [
    url(r'^admin/manage_number', admin_manage_number),
    url(r'^admin/manage_tenant', admin_manage_tenant),
    url(r'^admin/take_data', admin_take_data),
    url(r'^admin/service', admin_service),
    url(r'^admin/', admin.site.urls),

    url(r'^$', main),
    url(r'^action/(\d+)/',action),
    url(r'^rooms/',rooms),
    url(r'^services/',service),
    url(r'^service/(\d+)/',one_service),
    url(r'^reviews/',reviews),
    url(r'^send_review/',send_review),
    url(r'^about/',about),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
