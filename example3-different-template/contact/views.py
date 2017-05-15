from django.http import HttpResponseRedirect
from formtools.wizard.views import SessionWizardView

from contact.forms import ContactForm1, ContactForm2

FORMS = [
    ('info', ContactForm1),
    ('message', ContactForm2),
]

TEMPLATES = {
    'info': 'contact_info.html',
    'message': 'contact_message.html'
}

class ContactWizard(SessionWizardView):

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        do_something_with_the_form_data(form_list)
        return HttpResponseRedirect('/done/')

def do_something_with_the_form_data(form_list):
    """
    Do something, such as sending mail
    """
    form_data = [form.cleaned_data for form in form_list]

    print('#####')
    print('Subject: %s' % form_data[0]['subject'])
    print('Sender: %s' % form_data[0]['sender'])
    print('Message: %s' % form_data[1]['message'])
    print('#####')
