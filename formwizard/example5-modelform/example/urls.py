from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

from contact.views import ContactWizard, FORMS

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/', ContactWizard.as_view(FORMS)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
