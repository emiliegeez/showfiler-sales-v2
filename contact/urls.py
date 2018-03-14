from django.urls import path
from django.views.generic import TemplateView
from .views import ContactFormView
# from .forms import AkismetContactForm

# from .views import HomePage, ServicesPage

urlpatterns = [
    path('', ContactFormView.as_view(), name='contact'),
    path('sent/',
    TemplateView.as_view(
        template_name='contact_form_sent.html'),
        name='contact_form_sent'),
]
