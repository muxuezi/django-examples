import os

from django.conf import settings
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from formtools.wizard.views import SessionWizardView

from contact.forms import ContactForm1, ContactForm2, ContactForm3

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
    # Temporary storage file
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'files_temp'))

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        do_something_with_the_form_data(form_list)
        return render(self.request, 'done.html', {
            'form_data': [form.cleaned_data for form in form_list]
        })

def do_something_with_the_form_data(form_list):
    """
    Do something, such as sending mail
    """
    form_data = [form.cleaned_data for form in form_list]

    print('#####')
    print('Subject: %s' % form_data[0]['subject'])
    print('Sender: %s' % form_data[0]['sender'])
    print('Message: %s' % form_data[1]['message'])

    # If you have uploaded files, You need to save the files here
    # https://docs.djangoproject.com/en/1.10/topics/http/file-uploads/
    print('File: %s' % form_data[2]['files'])
    print('#####')
