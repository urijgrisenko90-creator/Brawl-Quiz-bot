import telebot
import os
from telebot.types import LabeledPrice, PreCheckoutQuery

# ТВОЙ ТОКЕН
TOKEN = '9118065614:AAEaf1RJ30lnMi4CHwuot6ZiFcwPIxU4Rzg'
bot = telebot.TeleBot(TOKEN)

# ТВОЯ ССЫЛКА НА ЧАТ
CHAT_LINK = 'https://t.me/Tosik552'

@bot.message_handler(commands=['start'])
def start(message):
    if 'pay' in message.text:
        # Выставляем счет на 50 звезд
        prices = [LabeledPrice(label='Доступ к чату', amount=50)]
        bot.send_invoice(
            message.chat.id,
            title='Доступ к чату',
            description='Оплатите 50 звезд, чтобы получить прямой чат с разработчиком.',
            invoice_payload='support_payment',
            provider_token='',  # Для Telegram Stars это поле оставляем пустым!
            currency='XTR',     # XTR - код валюты Telegram Stars
            prices=prices,
            start_parameter='pay'
        )
    else:
        bot.reply_to(message, "Привет! Это техподдержка Brawl Quiz 2.0. Если хочешь прямой чат с разработчиком, нажми кнопку в игре.")

@bot.pre_checkout_query_handler(func=lambda query: True)
def checkout(pre_checkout_query):
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True, error_message="Оплата не прошла, попробуйте позже.")

@bot.message_handler(content_types=['successful_payment'])
def got_payment(message):
    bot.send_message(message.chat.id, f'Спасибо за поддержку! Вот твоя ссылка на чат: {CHAT_LINK}')

# Необходимые команды для Telegram
@bot.message_handler(commands=['support'])
def support(message):
    bot.reply_to(message, "По любым вопросам пишите: @Tosik552")

@bot.message_handler(commands=['terms'])
def terms(message):
    bot.reply_to(message, "Оплачивая, вы соглашаетесь с правилами игры. Оплата за доступ к чату.")

@bot.message_handler(commands=['paysupport'])
def paysupport(message):
    bot.reply_to(message, "Вопросы по оплате: @Tosik552")

# Запуск бота
bot.infinity_polling()
