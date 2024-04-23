import requests
from bs4 import BeautifulSoup
import telebot
from telebot import types
from aiogram import Bot, Dispatcher, types

import time

from threading import Thread

import os
from config import token, id

bot = Bot(token)
dp = Dispatcher(bot)

# Создаем экземпляр бота
bot = telebot.TeleBot(token)


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, f"""😎 Здравствуй, я бот способный пересылать актуальные заказы на фриланс биржах в твои чаты. \nДля добавления меня в твой чат - пиши @DarthAnve\n\nСейчас я работаю в этих чатах:\nБИРЖА ВАКАНСИЙ АНВИ (https://t.me/+-UifmZqomSA0ZjZi)""")


def getSoupWithWrite(url):
    req = requests.get(url)
    with open('index.html', 'wt', encoding='utf-8') as file:
        file.write(req.text)
    soup = BeautifulSoup(req.text, 'lxml')
    return soup


def get_last_call():
    with open('lastOrder.log', 'rt') as file:
        last_call = file.read()
    return last_call

def getSoup(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    return soup


def sendNotification(message):
    url = "https://api.telegram.org/bot" + f'{token}'
    method = url + "/sendMessage"

    requests.post(method, data={
        "chat_id": int(id),
        "text": str(message)
    })


def parsHabrDesign():
    url = 'https://freelance.habr.com/tasks?only_with_price=true&categories=design_sites,design_landings,design_logos,design_illustrations,design_mobile,design_icons,design_polygraphy,design_banners,design_graphics,design_corporate_identity,design_presentations,design_modeling,design_animation,design_photo,design_other'
    soup = getSoup(url)
    all_table_task = soup.find_all(class_='task task_list')
    for item in all_table_task:
        nameTask = item.find(class_='task__title').find('a').get_text()
        urlTask = 'https://freelance.habr.com' + \
            item.find(class_='task__title').find('a').get('href')
        priceTask = item.find(class_='count').get_text()

        with open('lastOrder.log', 'r') as file:
            if nameTask in file.read():
                continue

        text = f"""#дизайн\n\nНа Habr появился новый заказ!\n\nНазвание: {nameTask};\n\nЦена: {priceTask};\n\nСсылка: {urlTask}"""
        sendNotification(text)

        with open('lastOrder.log', 'a') as file:
            file.write(nameTask + "\n")


def parsHabrDesignSafety():
    url = 'https://freelance.habr.com/tasks?only_with_price=true&safe_deal=true&categories=design_sites,design_landings,design_logos,design_illustrations,design_mobile,design_icons,design_polygraphy,design_banners,design_graphics,design_corporate_identity,design_presentations,design_modeling,design_animation,design_photo,design_other'
    soup = getSoup(url)
    all_table_task = soup.find_all(class_='task task_list')
    for item in all_table_task:
        nameTask = item.find(class_='task__title').find('a').get_text()
        urlTask = 'https://freelance.habr.com' + \
            item.find(class_='task__title').find('a').get('href')
        priceTask = item.find(class_='count').get_text()

        with open('lastOrder.log', 'r') as file:
            if nameTask in file.read():
                continue

        text = f"""🟢 #безопасная_сделка  #дизайн\n\nНа Habr появился новый заказ!\n\nНазвание: {nameTask};\n\nЦена: {priceTask};\n\nСсылка: {urlTask}"""
        sendNotification(text)

        with open('lastOrder.log', 'a') as file:
            file.write(nameTask + "\n")


def parsHabrContent():
    url = 'https://freelance.habr.com/tasks?only_with_price=true&categories=content_copywriting,content_rewriting,content_audio,content_article,content_scenarios,content_naming,content_correction,content_translations,content_coursework,content_specification,content_management,content_other'
    soup = getSoup(url)
    all_table_task = soup.find_all(class_='task task_list')
    for item in all_table_task:
        nameTask = item.find(class_='task__title').find('a').get_text()
        urlTask = 'https://freelance.habr.com' + \
            item.find(class_='task__title').find('a').get('href')
        priceTask = item.find(class_='count').get_text()

        with open('lastOrder.log', 'r') as file:
            if nameTask in file.read():
                continue

        text = f"""#контент\n\nНа Habr появился новый заказ!\n\nНазвание: {nameTask};\n\nЦена: {priceTask};\n\nСсылка: {urlTask}"""
        sendNotification(text)

        with open('lastOrder.log', 'a') as file:
            file.write(nameTask + "\n")


def parsHabrContentSafety():
    url = 'https://freelance.habr.com/tasks?only_with_price=true&safe_deal=true&categories=content_copywriting,content_rewriting,content_audio,content_article,content_scenarios,content_naming,content_correction,content_translations,content_coursework,content_specification,content_management,content_other'
    soup = getSoup(url)
    all_table_task = soup.find_all(class_='task task_list')
    for item in all_table_task:
        nameTask = item.find(class_='task__title').find('a').get_text()
        urlTask = 'https://freelance.habr.com' + \
            item.find(class_='task__title').find('a').get('href')
        priceTask = item.find(class_='count').get_text()

        with open('lastOrder.log', 'r') as file:
            if nameTask in file.read():
                continue

        text = f"""🟢 #безопасная_сделка  #контент\n\nНа Habr появился новый заказ!\n\nНазвание: {nameTask};\n\nЦена: {priceTask};\n\nСсылка: {urlTask}"""
        sendNotification(text)

        with open('lastOrder.log', 'a') as file:
            file.write(nameTask + "\n")


def parsHabrDevelopment():
    url = 'https://freelance.habr.com/tasks?only_with_price=true&categories=development_all_inclusive,development_backend,development_frontend,development_prototyping,development_ios,development_android,development_desktop,development_bots,development_games,development_1c_dev,development_scripts,development_voice_interfaces,development_other'
    soup = getSoup(url)
    all_table_task = soup.find_all(class_='task task_list')
    for item in all_table_task:
        nameTask = item.find(class_='task__title').find('a').get_text()
        urlTask = 'https://freelance.habr.com' + \
            item.find(class_='task__title').find('a').get('href')
        priceTask = item.find(class_='count').get_text()

        with open('lastOrder.log', 'r') as file:
            if nameTask in file.read():
                continue

        text = f"""#разработка\n\nНа Habr появился новый заказ!\n\nНазвание: {nameTask};\n\nЦена: {priceTask};\n\nСсылка: {urlTask}"""
        sendNotification(text)

        with open('lastOrder.log', 'a') as file:
            file.write(nameTask + "\n")


def parsHabrDevelopmentSafety():
    url = 'https://freelance.habr.com/tasks?only_with_price=true&safe_deal=true&categories=development_all_inclusive,development_backend,development_frontend,development_prototyping,development_ios,development_android,development_desktop,development_bots,development_games,development_1c_dev,development_scripts,development_voice_interfaces,development_other'
    soup = getSoup(url)
    all_table_task = soup.find_all(class_='task task_list')
    for item in all_table_task:
        nameTask = item.find(class_='task__title').find('a').get_text()
        urlTask = 'https://freelance.habr.com' + \
            item.find(class_='task__title').find('a').get('href')
        priceTask = item.find(class_='count').get_text()

        with open('lastOrder.log', 'r') as file:
            if nameTask in file.read():
                continue

        text = f"""🟢 #безопасная_сделка  #разработка\n\nНа Habr появился новый заказ!\n\nНазвание: {nameTask};\n\nЦена: {priceTask};\n\nСсылка: {urlTask}"""
        sendNotification(text)

        with open('lastOrder.log', 'a') as file:
            file.write(nameTask + "\n")


def parsHabrTesting():
    url = 'https://freelance.habr.com/tasks?only_with_price=true&categories=testing_sites,testing_mobile,testing_software'
    soup = getSoup(url)
    all_table_task = soup.find_all(class_='task task_list')
    for item in all_table_task:
        nameTask = item.find(class_='task__title').find('a').get_text()
        urlTask = 'https://freelance.habr.com' + \
            item.find(class_='task__title').find('a').get('href')
        priceTask = item.find(class_='count').get_text()

        with open('lastOrder.log', 'r') as file:
            if nameTask in file.read():
                continue

        text = f"""#тестирование\n\nНа Habr появился новый заказ!\n\nНазвание: {nameTask};\n\nЦена: {priceTask};\n\nСсылка: {urlTask}"""
        sendNotification(text)

        with open('lastOrder.log', 'a') as file:
            file.write(nameTask + "\n")


def parsHabrTestingSafety():
    url = 'https://freelance.habr.com/tasks?only_with_price=true&safe_deal=true&categories=testing_sites,testing_mobile,testing_software'
    soup = getSoup(url)
    all_table_task = soup.find_all(class_='task task_list')
    for item in all_table_task:
        nameTask = item.find(class_='task__title').find('a').get_text()
        urlTask = 'https://freelance.habr.com' + \
            item.find(class_='task__title').find('a').get('href')
        priceTask = item.find(class_='count').get_text()

        with open('lastOrder.log', 'r') as file:
            if nameTask in file.read():
                continue

        text = f"""🟢 #безопасная_сделка  #тестирование\n\nНа Habr появился новый заказ!\n\nНазвание: {nameTask};\n\nЦена: {priceTask};\n\nСсылка: {urlTask}"""
        sendNotification(text)

        with open('lastOrder.log', 'a') as file:
            file.write(nameTask + "\n")


def parsHabrAdmin():
    url = 'https://freelance.habr.com/tasks?only_with_price=true&categories=admin_servers,admin_network,admin_databases,admin_security,admin_other'
    soup = getSoup(url)
    all_table_task = soup.find_all(class_='task task_list')
    for item in all_table_task:
        nameTask = item.find(class_='task__title').find('a').get_text()
        urlTask = 'https://freelance.habr.com' + \
            item.find(class_='task__title').find('a').get('href')
        priceTask = item.find(class_='count').get_text()

        with open('lastOrder.log', 'r') as file:
            if nameTask in file.read():
                continue

        text = f"""#администрирование\n\nНа Habr появился новый заказ!\n\nНазвание: {nameTask};\n\nЦена: {priceTask};\n\nСсылка: {urlTask}"""
        sendNotification(text)

        with open('lastOrder.log', 'a') as file:
            file.write(nameTask + "\n")


def parsHabrAdminSafety():
    url = 'https://freelance.habr.com/tasks?only_with_price=true&safe_deal=true&categories=admin_servers,admin_network,admin_databases,admin_security,admin_other'
    soup = getSoup(url)
    all_table_task = soup.find_all(class_='task task_list')
    for item in all_table_task:
        nameTask = item.find(class_='task__title').find('a').get_text()
        urlTask = 'https://freelance.habr.com' + \
            item.find(class_='task__title').find('a').get('href')
        priceTask = item.find(class_='count').get_text()

        with open('lastOrder.log', 'r') as file:
            if nameTask in file.read():
                continue

        text = f"""🟢 #безопасная_сделка  #администрирование\n\nНа Habr появился новый заказ!\n\nНазвание: {nameTask};\n\nЦена: {priceTask};\n\nСсылка: {urlTask}"""
        sendNotification(text)

        with open('lastOrder.log', 'a') as file:
            file.write(nameTask + "\n")


def parsHabrMarketing():
    url = 'https://freelance.habr.com/tasks?only_with_price=true&categories=marketing_smm,marketing_seo,marketing_context,marketing_email,marketing_research,marketing_sales,marketing_pr,marketing_other'
    soup = getSoup(url)
    all_table_task = soup.find_all(class_='task task_list')
    for item in all_table_task:
        nameTask = item.find(class_='task__title').find('a').get_text()
        urlTask = 'https://freelance.habr.com' + \
            item.find(class_='task__title').find('a').get('href')
        priceTask = item.find(class_='count').get_text()

        with open('lastOrder.log', 'r') as file:
            if nameTask in file.read():
                continue

        text = f"""#маркетинг\n\nНа Habr появился новый заказ!\n\nНазвание: {nameTask};\n\nЦена: {priceTask};\n\nСсылка: {urlTask}"""
        sendNotification(text)

        with open('lastOrder.log', 'a') as file:
            file.write(nameTask + "\n")


def parsHabrMarketingSafety():
    url = 'https://freelance.habr.com/tasks?only_with_price=true&safe_deal=true&categories=marketing_smm,marketing_seo,marketing_context,marketing_email,marketing_research,marketing_sales,marketing_pr,marketing_other'
    soup = getSoup(url)
    all_table_task = soup.find_all(class_='task task_list')
    for item in all_table_task:
        nameTask = item.find(class_='task__title').find('a').get_text()
        urlTask = 'https://freelance.habr.com' + \
            item.find(class_='task__title').find('a').get('href')
        priceTask = item.find(class_='count').get_text()

        with open('lastOrder.log', 'r') as file:
            if nameTask in file.read():
                continue

        text = f"""🟢 #безопасная_сделка  #маркетинг\n\nНа Habr появился новый заказ!\n\nНазвание: {nameTask};\n\nЦена: {priceTask};\n\nСсылка: {urlTask}"""
        sendNotification(text)

        with open('lastOrder.log', 'a') as file:
            file.write(nameTask + "\n")


def parsHabrOther():
    url = 'https://freelance.habr.com/tasks?only_with_price=true&categories=other_audit_analytics,other_consulting,other_jurisprudence,other_accounting,other_audio,other_video,other_engineering,other_other'
    soup = getSoup(url)
    all_table_task = soup.find_all(class_='task task_list')
    for item in all_table_task:
        nameTask = item.find(class_='task__title').find('a').get_text()
        urlTask = 'https://freelance.habr.com' + \
            item.find(class_='task__title').find('a').get('href')
        priceTask = item.find(class_='count').get_text()

        with open('lastOrder.log', 'r') as file:
            if nameTask in file.read():
                continue

        text = f"""#разное\n\nНа Habr появился новый заказ!\n\nНазвание: {nameTask};\n\nЦена: {priceTask};\n\nСсылка: {urlTask}"""
        sendNotification(text)

        with open('lastOrder.log', 'a') as file:
            file.write(nameTask + "\n")


def parsHabrOtherSafety():
    url = 'https://freelance.habr.com/tasks?only_with_price=true&safe_deal=true&categories=other_audit_analytics,other_consulting,other_jurisprudence,other_accounting,other_audio,other_video,other_engineering,other_other'
    soup = getSoup(url)
    all_table_task = soup.find_all(class_='task task_list')
    for item in all_table_task:
        nameTask = item.find(class_='task__title').find('a').get_text()
        urlOrder = 'https://freelance.habr.com' + \
            item.find(class_='task__title').find('a').get('href')
        priceTask = item.find(class_='count').get_text()

        with open('lastOrder.log', 'r') as file:
            if nameTask in file.read():
                continue

        text = f"""🟢 #безопасная_сделка  #разное\n\nНа Habr появился новый заказ!\n\nНазвание: {nameTask};\n\nЦена: {priceTask};\n\nСсылка: {urlOrder}"""
        sendNotification(text)

        with open('lastOrder.log', 'a') as file:
            file.write(nameTask + "\n")


def startHabr():
    print('Парсинг Habr запускается.')

    while True:
        try:
            parsHabrContent()
            time.sleep(60)
            parsHabrDesign()
            time.sleep(65)
            parsHabrDevelopment()
            time.sleep(77)
            parsHabrAdmin()
            time.sleep(50)
            parsHabrMarketing()
            time.sleep(70)
            parsHabrOther()
            time.sleep(80)
            parsHabrTesting()
            time.sleep(53)
            parsHabrDevelopmentSafety()
            time.sleep(77)
            parsHabrContentSafety()
            time.sleep(60)
            parsHabrDesignSafety()
            time.sleep(65)
            parsHabrAdminSafety()
            time.sleep(50)
            parsHabrMarketingSafety()
            time.sleep(70)
            parsHabrOtherSafety()
            time.sleep(80)
            parsHabrTestingSafety()
            time.sleep(53)
        except requests.exceptions.ConnectionError:
            print(
                'Не удалось установить соединение с сервером. Проверьте подключение с интернетом.')
            continue


def main():
    print('Бот запускается')

    if not os.path.exists('lastOrder.log'):
        with open('lastOrder.log', 'wt') as file:
            file.write('Start\n')
        print('Файл log создан')

    threadHabr = Thread(target=startHabr)

    threadHabr.start()


if __name__ == "__main__":
    main()

bot.polling()