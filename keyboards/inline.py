from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def first_question_u7():
    ikb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text='Pele', callback_data='1')
    ],[InlineKeyboardButton(text='Maradona', callback_data='2')]]
    )
    return ikb