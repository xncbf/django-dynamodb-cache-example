import random
from django.shortcuts import render
from django.views.decorators.cache import cache_page


@cache_page(5)
def my_view(request):
    return render(request, 'index.html', {'random_number': random.randint(1, 100)})
