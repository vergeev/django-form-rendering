from django.views.generic import FormView

from contacts.forms import ContactForm


class Home(FormView):
    form_class = ContactForm
    template_name = 'home.html'
