from django.shortcuts import render


def platform_index(request):
    return render(request, 'fourth_task/platform.html',
                  {'header': 'Главная страница'})


def catalog(request):
    return render(request, 'fourth_task/games.html',
                  {'header': 'Игры',
                   'games': ['Atomic Heart',
                             'Cyberpank 2077',
                             'PayDay 2']})


def cart(request):
    return render(request, 'fourth_task/cart.html', {'header': 'Корзина'})
