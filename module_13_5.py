# Задача "Меньше текста, больше кликов":
# Необходимо дополнить код предыдущей задачи, чтобы вопросы о параметрах тела для расчёта калорий
# выдавались по нажатию кнопки.
# Измените massage_handler для функции set_age. Теперь этот хэндлер будет реагировать на текст
# 'Рассчитать', а не на 'Calories'.
# Создайте клавиатуру ReplyKeyboardMarkup и 2 кнопки KeyboardButton на ней со следующим текстом:
# 'Рассчитать' и 'Информация'. Сделайте так, чтобы клавиатура подстраивалась под размеры интерфейса
# устройства при помощи параметра resize_keyboard.
# Используйте ранее созданную клавиатуру в ответе функции start, используя параметр reply_markup.
# В итоге при команде /start у вас должна присылаться клавиатура с двумя кнопками. При нажатии на кнопку
# с надписью 'Рассчитать' срабатывает функция set_age с которой начинается работа машины состояний для age,
# growth и weight.
from aiogram import Bot, dispatcher, executor, types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext
import asyncio

api = ""
bot = Bot(token = api)
dp = Dispatcher(bot, storage= MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard = True)
button = KeyboardButton(text = "Рассчитать")
button2 = KeyboardButton(text = "Информация")

kb.row(button, button2)

@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer("Hi,", reply_markup = kb)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text='Рассчитать')
async def set_age(message):
    await message.answer("Введите Ваш возраст цифрой:")
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer("Введите Ваш рост в см:")
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес в кг:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def rec_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    rec_calor_woman = (10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) - 161)
    rec_calor_man = (10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5)
    await message.answer(f'Ваша норма калорий: {rec_calor_woman} ккал в сутки (для женщин)')
    await message.answer(f'Ваша норма калорий: {rec_calor_man} ккал в сутки (для мужчин)')

    @dp.message_handler(text='Информация')
    async def set_age(message):
        await message.answer(f"Ваша норма калорий: {rec_calor_woman} Срочно садитесь на диету!")

    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
