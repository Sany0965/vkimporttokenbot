import telebot
from telebot import types
import requests

from vkaudiotoken import get_kate_token, get_vk_official_token

TOKEN = 'ТОКЕНОТБОТФАЗЕР'
bot = telebot.TeleBot(TOKEN)


def is_valid_vk_token(token):
    api_url = "https://api.vk.com/method/users.get"
    params = {
        'access_token': token,
        'v': '5.131',
    }
    response = requests.get(api_url, params=params)
    data = response.json()
    if 'error' in data:
        return False
    else:
        return True


def get_vk_profile_url(access_token):
    response = requests.get('https://api.vk.com/method/users.get', params={'access_token': access_token, 'v': '5.131'})
    data = response.json()
    user_id = data['response'][0]['id']
    profile_url = f'https://vk.com/id{user_id}'
    return profile_url



@bot.message_handler(commands=['start'])
def send_welcome(message):
    username = message.from_user.first_name
    markup = types.InlineKeyboardMarkup()
    token_button = types.InlineKeyboardButton(text="📄Получить", callback_data="get_token")
    dev_button = types.InlineKeyboardButton(text="🟠Dev", url="https://t.me/pizzaway")
    markup.add(token_button, dev_button)
    bot.send_message(message.chat.id, f"Добрый день, {username}! Я помогу Вам получить access token (Токен) от ВКонтакте!\nЖмите кнопку '📄Получить', чтобы начать!\n🟥Важно! Если у вас на аккаунте стоит 2FA (двухфакторная авторизация), Бот не сможет получить токен!", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "get_token")
def ask_for_login(callback_query):
    bot.answer_callback_query(callback_query.id)
    msg = bot.send_message(callback_query.message.chat.id, "Пожалуйста, напишите ВАШ НОМЕР 📲:")
    bot.register_next_step_handler(msg, process_login_step)


def process_login_step(message):
    login = message.text
    msg = bot.send_message(message.chat.id, "Пожалуйста, напишите Ваш пароль 🔐:")
    bot.register_next_step_handler(msg, process_password_step, login)


def process_password_step(message, login):
    password = message.text
    try:
        kate_token = get_kate_token(login, password)['token']
        vk_token = get_vk_official_token(login, password)['token']
        bot.send_message(message.chat.id, f"<b>Ваши токены:</b>\n\n"
                                          f"<b>Получен через user_agent KateMobileAndroid🤖:</b>\n<code>{kate_token}</code>\n\n"
                                          f"<b>Получен через user_agent VKAndroidApp🐟 (рекомендуется):</b>\n<code>{vk_token}</code>\n\n"
                                          f"<i>⛔️Пожалуйста, не передавайте его никому, если не знаете что с ним делать!\n" 
                                          f"Если вы случайно его передали, смените пароль, тогда токен аннулируется!</i>", parse_mode='HTML')
    except Exception as e:
        bot.send_message(message.chat.id, "⛔️Пожалуйста, проверьте данные, логин или пароль неверны!")


@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = "Токен доступа к странице пользователя ВКонтакте предоставляет приложениям или скриптам доступ к определенным данным и действиям на странице пользователя, таким как чтение информации профиля, отправка сообщений и другие.\n\n" \
                "Чтобы получить токен доступа, обычно используется метод аутентификации, например, OAuth. Пользователь предоставляет приложению разрешения на доступ к своей странице, и в ответ получает специальный токен доступа. Этот токен нужно хранить в безопасности, так как он дает доступ к личной информации пользователя.\n\n" \
                "Используйте токен в своих скриптах или приложениях осторожно и в соответствии с правилами использования данных, установленными ВКонтакте.\n\n" \
                "🔑✨"
    bot.send_message(message.chat.id, help_text)


bot.polling(none_stop=True)
