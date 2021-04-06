from django.urls import path
from . import views #import views


# adding url
urlpatterns = [
    path('', views.index, name='home'), #home
    path('portfolio', views.portfolio, name='portfolio'), #portfolio
    path('sobre', views.sobre, name='sobre'), #about
    path('contact', views.contact, name='contact'), #contact

]