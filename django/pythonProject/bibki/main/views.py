from django.shortcuts import render
from django.http import HttpResponse
from .pogoda import get_data

def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['* Главное меню - место ознакомления с сайтом',
                   '* Про нас - место подписи авторства и работы с анимацией',
                   '* Погода - пример работы со сторонними API',
                   '* Новости - реализация функционирования БД'],
    }
    # return HttpResponse("<h4>Проверка работы</h4>")
    return render (request, 'main/index.html', data)
def about(request):
    # return HttpResponse("<h4>тест вывод информации</h4>")
    return render(request, 'main/about.html')

def weather_view(request):
    city = request.GET.get('city', '')  # Получение значения города из параметров запроса
    weather_data = None

    if city:
        weather_data = get_data(city)  # Передача города в функцию для получения данных о погоде
    return render(request, 'main/weather.html', {'weather': weather_data})