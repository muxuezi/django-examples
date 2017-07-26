import os

from django.conf import settings
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from formtools.wizard.views import SessionWizardView

from .forms import ContactForm1, ContactForm2, ContactForm3
from .models import Contact

FORMS = [
    ('info', ContactForm1),
    ('message', ContactForm2),
    ('file', ContactForm3),
]

TEMPLATES = {
    'info': 'contact_info.html',
    'message': 'contact_message.html',
    'file': 'contact_file.html'
}

class ContactWizard(SessionWizardView):
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'files_temp'))
    instance = None

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def get_form_instance(self, step):
        """
        get ModelForm
        """
        if self.instance is None:
            self.instance = Contact()
        return self.instance

    def done(self, form_list, **kwargs):

        self.instance.save() # save data

        return render(self.request, 'done.html', {
            'form_data': [form.cleaned_data for form in form_list]
        })
