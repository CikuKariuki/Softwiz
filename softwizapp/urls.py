from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.home, name='home'),
    url(r'^aboutus/',views.aboutus, name='aboutus'),
    url(r'^products/',views.products, name='products'),
    url(r'^contact/',views.contact, name='contact'),

]