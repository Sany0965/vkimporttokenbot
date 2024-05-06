# VK Access Token Bot

Этот бот поможет вам получить access token (токен доступа) от ВКонтакте, используя ваш номер телефона и пароль. Access token предоставляет доступ к определенным данным и действиям на вашей странице ВКонтакте, таким как чтение информации профиля и отправка сообщений.

## Библиотеки

Для работы бота используются следующие библиотеки:

- [telebot](https://github.com/eternnoir/pyTelegramBotAPI): Библиотека для создания ботов Telegram на Python.
- [requests](https://github.com/psf/requests): Простая библиотека для выполнения HTTP-запросов.
- [vkaudiotoken](https://github.com/LonamiWebs/vk-audio-token): Библиотека для получения access token от ВКонтакте.

## Установка

Для установки библиотек выполните следующие команды:

```bash
pip install pyTelegramBotAPI requests
pip install vkaudiotoken
```

## Запуск бота

1. Укажите токен вашего бота Telegram в переменной `TOKEN` в файле `main.py`.
2. Запустите бота, выполнив файл `main.py`.

```bash
python main.py
```

## Получение токена

1. Отправьте боту команду `/start`.
2. Нажмите кнопку "📄Получить".
3. Следуйте инструкциям для ввода вашего номера телефона и пароля от ВКонтакте.
4. Получите токен доступа.

## Важно

- Будьте осторожны с вашим токеном доступа, не передавайте его третьим лицам.
- Если вы случайно передали токен, рекомендуется сменить пароль в ВКонтакте, чтобы аннулировать токен.

## Авторство

Этот бот был создан [PIZZAWAY](https://t.me/pizzaway).
