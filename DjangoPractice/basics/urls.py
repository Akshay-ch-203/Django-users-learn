from django.urls import path
from basics.views import index


urlpatterns = [
    path('', index, name='index')
]
