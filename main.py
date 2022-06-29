import config
import logging

from aiogram import Bot, Dispatcher, executor, types

# задаем уровень логов
logging. basicConfig(level=logging. INFO)

# инициализируем бота
bot = Bot(token=config.API_TOKEN)
dp = Dispatcher (bot)

# Эхо
@dp.message_handler()
async def echo(message: types.Message):
| ЕЕВС «5 4)
iL
# запускаем лонг поллинг
if _ пате__ ШЕИ 95
executor.start_polling(dp, skip_updates=True)