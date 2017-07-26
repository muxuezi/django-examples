from django.shortcuts import render
from formtools.wizard.views import SessionWizardView

from contact.forms import ContactForm1, ContactForm2

class ContactWizard(SessionWizardView):
    template_name = 'contact.html'
    form_list = [ContactForm1, ContactForm2]

    def done(self, form_list, **kwargs):
        return render(self.request, 'done.html', {
            'form_data': [form.cleaned_data for form in form_list]
        })
