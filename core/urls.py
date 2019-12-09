from django.urls import path

from .views import HomeView, AuthorizeView, CallbackView

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('authorize/', AuthorizeView.as_view(), name='authorize'),
    path('callback/', CallbackView.as_view(), name='callback'),
]
