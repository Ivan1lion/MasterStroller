from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

handlers_router = Router()


@handlers_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text="Привет")


@handlers_router.message(Command("privacy"))
async def cmd_privacy(message: Message):
    await message.answer(f'Этот документ описывает политику конфиденциальности для бота @MasterStroller_Bot '
                         f'(👨🏻‍🔧 Master Stroller 🚼)'
                         f'\n\n<b>Собираемая информация</b>'
                         f'\nМы собираем следующие данные:'
                         f'\n- Данные указанные в профиле, такие как номер телефона и Username пользователя '
                         f'(это необходимо для реализации связи между продавцом и пользователем)'
                         f'\n- Сообщения, отправленные боту'
                         f'\n\n<b>Использование данных</b>'
                         f'\nСобранные данные используются для:'
                         f'\n- Обработки запросов пользователей'
                         f'\n- Улучшения работы бота'
                         f'\n- Анализа использования сервиса'
                         f'\n\n<b>Хранение данных</b>'
                         # f'\nДанные хранятся на сервере без срока хранения'
                         f'\nДанные хранятся на сервере до остановки бота. После чего данные удаляются'
                         f'\n\n<b>Передача данных третьим лицам</b>'
                         # f'\nМы не передаем ваши данные третьим лицам без вашего согласия, за исключением случаев, '
                         # f'предусмотренных законом'
                         f'\nИспользуя данный бот вы подтверждаете согласие на передачу ваших данных третьим лицам '
                         f'(пользователям бота), а именно вашего номера телефона и Username. Это необходимо для того '
                         f'что бы вы могли связаться с клиентамии и предложить свой товар'
                         f'\n\n<b>Изменения в политике конфиденциальности</b>'
                         f'\nМы оставляем за собой право обновлять эту политику. Обо всех изменениях мы уведомим '
                         f'вас через наш бот'
                         f'\n\n<b>Контактная информация</b>'
                         f'\nЕсли у вас есть вопросы, свяжитесь с нами @...')
