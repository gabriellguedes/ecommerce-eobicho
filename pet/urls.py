from django.conf.urls import url, include
from pet.views import home
urlpatterns = [
    url(r'^$', home ,name='home'),
    
]