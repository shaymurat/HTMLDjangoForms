from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

# Create your views here.

users = {'Василий': {'password': '12230823', 'age': 23},
         'Елена': {'password': 'qwerty123', 'age': 18},
         'Тимур': {'password': '1|Awv&8jRv', 'age': 19},
         'marina': {'password': '00112233', 'age': 27}}


def sign_up_by_html(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        error = ''
        if password != repeat_password:
            error = 'Пароли не совпадают'
        elif age < 18:
            error = 'Вы должны быть старше 18'
        elif username in users:
            error = 'Пользователь уже существует'

        if error:
            return render(request, 'fifth_task/registration_page.html',
                          {'error': error, 'username': username, 'age': age})
        else:
            users[username] = {'password': password, 'age': age}
            return HttpResponse(f'Приветствуем, {username}!')

    return render(request, 'fifth_task/registration_page.html')


def sign_up_by_django(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            error = ''
            if password != repeat_password:
                error = 'Пароли не совпадают'
                form.fields['password'].widget.attrs.update(
                    {'autofocus': '', 'class': 'col_input'})
                form.fields['repeat_password'].widget.attrs.update(
                    {'class': 'col_input'})
            elif age < 18:
                error = 'Вы должны быть старше 18'
                form.fields['age'].widget.attrs.update(
                    {'autofocus': '', 'class': 'col_input'})
            elif username in users:
                error = 'Пользователь уже существует'
                form.fields['username'].widget.attrs.update(
                    {'autofocus': '', 'class': 'col_input'})

            if error:
                return render(request, 'fifth_task/registration_page.html',
                              {'error': error, 'form': form})
            else:
                users[username] = {'password': password, 'age': age}
                return HttpResponse(f'Приветствуем, {username}!')
    else:
        return render(request, 'fifth_task/registration_page.html',
                      {'form': UserRegister()})
