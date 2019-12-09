import random
from urllib.parse import urlencode
from uuid import uuid4

from django.conf import settings
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, View

from .forms import AuthorizeForm


class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['image'] = random.choice([
            'https://media.giphy.com/media/QOYjGrYSuBMAg/giphy.gif',
            'https://media.giphy.com/media/9Si6HlM5DfsA0/giphy.gif',
            'https://media.giphy.com/media/pejdqIYGcxHMY/giphy.gif',
        ])

        return context_data


class AuthorizeView(View):
    @staticmethod
    def post(request: HttpRequest) -> HttpResponse:
        form = AuthorizeForm(request.POST)

        if not form.is_valid():
            return HttpResponseBadRequest('Form is not valid')

        subdomain = form.cleaned_data['subdomain']

        url = f'https://{subdomain}.myshopify.com/admin/oauth/authorize?' + urlencode({
            'client_id': settings.SHOPIFY_API_KEY,
            'scope': 'read_products,read_orders',
            'redirect_uri': request.build_absolute_uri(reverse('core:callback')),
            'state': uuid4(),
        })

        return HttpResponseRedirect(url)


class CallbackView(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        return HttpResponse('Hello, Callback!')
