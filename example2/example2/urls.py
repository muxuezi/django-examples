from django.conf.urls import url

from contact.views import ContactWizard

urlpatterns = [
    url(r'^contact/', ContactWizard.as_view()),
]
