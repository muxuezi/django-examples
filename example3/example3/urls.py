from django.conf.urls import url
from django.views.generic import TemplateView

from contact.views import ContactWizard, FORMS

urlpatterns = [
    url(r'^contact/', ContactWizard.as_view(FORMS)),
    url(r'^done/', TemplateView.as_view(template_name='done.html')),
]
