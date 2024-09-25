import asyncio
from playwright.async_api import async_playwright, Page
from time import sleep
import keyboard
import sys
# import proverka_based

# Основная идея - симуляция того что человек функционирует через браузер
async def main():
    async with async_playwright() as playwright:
        # Запускаем браузер с графическим интерфейсом
        browser = await playwright.chromium.launch(headless=False)
        # Создаем новую страницу
        page = await browser.new_page()
        # Вывести подключение браузера
        if browser.is_connected()==True: print('Connected succesfull','True')
        else: print ('Connected destroyed or wasnt succesfull')

        # Загружаем страницу *****В КАВЫЧКАХ*****
        await page.goto('https://nations-conflict.ru/')

        # Функция захода в игру
        sleep(1)
        print('Началась процедура логина')
        async def login():
            await page.get_by_placeholder("id_login (цифры)").fill("16216479")
            sleep(0.5)
            await page.get_by_placeholder("пароль").fill("fN(Om6x)")
            sleep(0.5)
            await page.get_by_role("button").click()
            await page.get_by_role("cell", name="На главную").get_by_role("link").click()
            sleep(1)
            # Функция храма
        async def church():
            await page.get_by_text("Храм").click(); sleep(0.5)
            await page.get_by_text("Начать!").click() #С кнопок считыывает параметр value
        # РАБота с войсками
        async def voyska():
            await page.get_by_role("link", name="Войска").click(); sleep(1)
            await page.get_by_text("Отряды").click(); sleep(1)
            await page.locator(".item_5").first.click(); sleep (2)
            await page.get_by_alt_text("Идти").click(); sleep(1)
            await page.get_by_role("link", name="Войска").click()
            sleep(0.5)
            for i in range(2,5):
                await page.locator(f"tr:nth-child({i}) > .recruit_item_title > .item_5").click(); sleep (1)
                await page.get_by_alt_text("Идти").click(); sleep(1)
                await page.get_by_role("link", name="Войска").click(); sleep(1)
        await login()
        # await church()
        await voyska()
        # Можно добавить другие действия, например, получение текста элемента или скриншот страницы
        # Закрываем браузер
        keyboard.wait('q'); await browser.close(); print('Остановка выполнения по нажатию. Принудительная'); sys.exit()


# Запускаем основную функцию
asyncio.run(main())
