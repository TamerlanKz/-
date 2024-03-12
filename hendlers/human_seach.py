from aiogram import types, F, Router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keybord.prof_keybords import make_row_keyboard



router = Router()


human_gender  = ["Man", "Woman"]
human_years= ["10-15", "16-20", "21-30","30-45"]

class SeachHuman(StatesGroup):
    search_human_gender = State()
    search_human_years = State() 


#Хэндлер на команду /Приступим к поиску!)
@router.message(Command('human'))
async def cmd_seach(message: types.Message, state: FSMContext):
    name=message.from_user.first_name
    await message.answer(
    f'Привет, {name}, Выбери какого пола?',reply_markup=make_row_keyboard(human_gender)
    )
    await state.set_state(SeachHuman.search_human_gender
)



@router.message(SeachHuman.search_human_gender, F.text.in_ (human_gender))
async def cmd_seach_age (message: types.Message, state: FSMContext):
    await state.update_data(choose_gender=message.text.lower())
    await message.answer(f'перейдем на следующий уровень',reply_markup=make_row_keyboard(human_years)
    )
    await state.set_state(SeachHuman.search_human_years)

@router.message(SeachHuman.search_human_years)
async def cmd_seach_in_cerektor(message: types.Message):
    await message.answer(
    f'Привет, {message.from_user.first_name}, Выбери какого пола?Я предоставил вам клвиатуру'
    ,reply_markup=make_row_keyboard(human_gender)
    )
   

   
@router.message(SeachHuman.search_human_years, F.text.in_ (human_years))
async def cmd_seach_finish (message: types.Message, state: FSMContext):
    await state
    await message.answer(f'Спосибо, возрост приблезительно {message.text.lower()},вы ищите   {state.user_data.get("human_gender")}')
    await state.set_state(SeachHuman.search_human_years)
    reply_markup=make_row_keyboard(human_years)


