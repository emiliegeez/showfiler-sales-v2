from django.urls import path

from .views import HomePage, ServicesPage

urlpatterns = [
    path('', HomePage.as_view(template_name="index.html"), name='home'),
    path('services/', ServicesPage.as_view(template_name="services.html"), name='services'),
    path('about/', ServicesPage.as_view(template_name="about-us.html"), name='about'),
]
