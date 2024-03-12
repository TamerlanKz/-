import asyncio
from config_API import token1
from aiogram import Bot, Dispatcher, types, F
import logging
from hendlers import coomand , corer_choise ,  human_seach 


async def main():
    # Включаем логгирование
    logging.basicConfig(level=logging.INFO)

    # Создаем объект бота
    bot = Bot(token=token1)

    # Диспечер
    dp = Dispatcher()
    dp.include_router(human_seach.router)
    dp.include_router(corer_choise.router)
    dp.include_router(coomand.router)
    

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
