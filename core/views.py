import random

from django.views.generic import TemplateView


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
