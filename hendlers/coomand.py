from aiogram import types, F, Router
from aiogram.filters.command import Command
import logging
import random
from keybord.keybord_simpa import kb1, kb2
from utils.random_fox import fox
from utils.soup import winter


router = Router()


#Хэндлер на команду /start
@router.message(Command('start'))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Привет, {name}', reply_markup=kb1)


#Хэндлер на команду /stop
@router.message(Command('stop'))
async def cmd_stop(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Пока, {name}')
    await message.answer_sticker('CAACAgIAAxkBAAELpMRl7AjHDwdSqwi1_Y1WqAK6Wnnx3QACPAkAAgedAAFINTMb17qZWDw0BA')

#Хэндлер на команду /wenter
@router.message(Command('wenter'))
async def cmd_wenter(message: types.Message):
    await message.answer(f'В моем любимом городе  {winter()}' )
    #await message.answer_sticker('CAACAgIAAxkBAAELpMRl7AjHDwdSqwi1_Y1WqAK6Wnnx3QACPAkAAgedAAFINTMb17qZWDw0BA')

#Хэндлер на команду /fox
@router.message(Command('fox'))
@router.message(Command('лиса'))
@router.message(F.text.lower() == 'покажи лису')
async def cmd_fox(message: types.Message):
    name = message.chat.first_name
    img_fox = fox()
    await message.answer(f'Держи лису, {name}')
    await message.answer_photo(photo=img_fox)
# await message.answer_
# await bot.send_photo(message.from_user.id, photo=img_fox)



#Хендлер на сообщения
@router.message(F.text)
async def msg_echo(message: types.Message):
    msg_user = message.text.lower()
    name = message.chat.first_name
    if 'привет' in msg_user:
        await message.answer(f'Привет-привет, {name}')
    elif 'пока' == msg_user:
        await message.answer(f'Пока-пока, {name}')
    elif "кинуть кость" in msg_user:
        await message.answer(f'ny че народ погнали!!!!')
        await message.answer_dice(emoji="🎲")
    elif 'лиса' in msg_user:
        await message.answer(f'Смотри что у меня есть, {name}', reply_markup=kb2)
    elif 'wenter' in msg_user:
        await message.answer(f'Погода в моем любимом городе {winter()}')
    else:
        await message.answer(f'Я не знаю такого слова')