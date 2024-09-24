import requests
from lxml import html
# # # Имитация pogoda.py для теста

def get_temperature_from_google(city_name):
    # Создание URL для поиска в Google
    url = f"https://www.google.com/search?q=temperature+{city_name}"

    # Заголовки, чтобы имитировать запрос от браузера
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Выполнение запроса
    response = requests.get(url, headers=headers)

    # Проверка статуса ответа
    if response.status_code != 200:
        return "Ошибка получения данных"

    # Получение HTML-кода
    html_content = response.text

    # Парсинг HTML-кода с помощью lxml
    tree = html.fromstring(html_content)

    # Полный XPath для поиска температуры
    temp_xpath = '//*[@id="wob_tm"]'

    # Извлечение элемента с помощью XPath
    temp_element = tree.xpath(temp_xpath)

    if temp_element:
        return f"Температура в {city_name}: {temp_element[0].text}°C"
    else:
        return "Температура не найдена"


# Пример использования функции
if __name__ == "__main__":
    city = "Moscow"  # Замените на нужный город
    temperature = get_temperature_from_google(city)
    print(temperature)





# import requests
# from lxml import html
#
#
# def get_temperature(city_name):
#     # URL для запроса
#     search_url = f"https://www.google.com/search?q=temperature+{city_name}"
#
#     # Выполнение запроса
#     response = requests.get(search_url)
#
#     print(response.status_code)
#     # Проверка статуса ответа
#     if response.status_code != 200:
#         return "Ошибка получения данных"
#
#     # Получение HTML-кода
#     html_content = response.text
#
#     # Парсинг HTML-кода с помощью lxml
#     tree = html.fromstring(html_content)
#
#     # XPath для поиска элемента с температурой
#     xpath_expr = '//*[@id="wob_tm"]'
#     temp_value = tree.xpath(xpath_expr)
#     print('value:',temp_value)
#
#     if temp_value:
#         # Извлечение текста из первого найденного элемента
#         temperature = temp_value[0].text.strip()
#         return temperature
#     else:
#         return "Данные по температуре в данный момент не могут быть подгружены"
#
#
# # Пример использования функции
# if __name__ == "__main__":
#     city = "omsk"
#     temperature = get_temperature(city)
#     print(f"Температура в {city}: {temperature}")

import requests
from lxml import html


def get_temperature_from_google(city_name):
    # Создание URL для поиска в Google
    url = f"https://www.google.com/search?q=temperature+{city_name}&hl=ru"

    # Заголовки, чтобы имитировать запрос от браузера
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Выполнение запроса
    response = requests.get(url, headers=headers)
    print(response.status_code)
    # Проверка статуса ответа
    if response.status_code != 200:
        return "Ошибка получения данных"

    # Получение HTML-кода
    html_content = response.text
    tree = html.fromstring(html_content)

    # Полный XPath для поиска температуры
    temp_xpath = '//*[@id="wob_tm"]'
    temp_element = tree.xpath(temp_xpath)
    print(temp_element)
    temp_xpath = '//*[@id="wob_dts"]'
    temp_datetime = tree.xpath(temp_xpath)
    print(temp_datetime)
    temp_xpath = '//span[@class="BBwThe"]'
    temp_city = tree.xpath(temp_xpath)
    print(temp_city)

    temp_xpath = '//*[@id="wob_pp"]'
    temp_other1 = tree.xpath(temp_xpath)
    print(temp_other1)

    temp_xpath = '//*[@id="wob_hm"]'
    temp_other2 = tree.xpath(temp_xpath)
    print(temp_other2)

    temp_xpath = '// *[@id="wob_ws"]'
    temp_other3 = tree.xpath(temp_xpath)
    print(temp_other3)

    temp_xpath = '//*[@id="wob_dc"]'
    temp_resume = tree.xpath(temp_xpath)
    print(temp_resume)

    if temp_element:
        return {
            'temp_element': f"{temp_city[0].text} Температура: {temp_element[0].text}°C",
            'temp_datetime': f"{temp_datetime[0].text}",
            'temp_other1': f"Вероятность осадков: {temp_other1[0].text}",
            'temp_other2': f"Влажность: {temp_other2[0].text}",
            'temp_other3': f"Ветер: {temp_other3[0].text}",
            'temp_resume': f"{temp_resume[0].text}"
        }
    else:
        return "Температура не найдена"


# Пример использования функции
if __name__ == "__main__":
    city = "Москва"  # Замените на нужный город
    temperature = get_temperature_from_google(city)
    print(temperature)
