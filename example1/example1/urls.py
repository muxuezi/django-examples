from django.conf.urls import url

from contact.forms import ContactForm1, ContactForm2
from contact.views import ContactWizard

urlpatterns = [
    url(r'^contact/', ContactWizard.as_view([ContactForm1, ContactForm2])),
]
