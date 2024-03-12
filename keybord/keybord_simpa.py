from aiogram import types


button1 = types.KeyboardButton(text='/start')
button2 = types.KeyboardButton(text='/prof')
button3 = types.KeyboardButton(text='/stop')
button4 = types.KeyboardButton(text='Покажи лису')
button5 = types.KeyboardButton(text='/human')
button6 = types.KeyboardButton(text='Кинуть кость ')
button7 = types.KeyboardButton(text='/wenter') 
keyboard1 = [
[button1, button2, button3],
[button4],
[button5,button7],
[button6]
]

keyboard2 = [
[button3, button4],
]

kb1 = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)
kb2 = types.ReplyKeyboardMarkup(keyboard=keyboard2, resize_keyboard=True)