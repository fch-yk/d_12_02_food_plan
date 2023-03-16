from django.shortcuts import render
from django.views import View

class Index(View):
    """Представление главной страницы"""
    template_name = 'food/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
