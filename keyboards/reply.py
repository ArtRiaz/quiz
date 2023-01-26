from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType

def get_kb():
    kb = ReplyKeyboardMarkup(keyboard=[[
        KeyboardButton(text='Commencer le quizz', request_poll=KeyboardButtonPollType())
    ]])
    return kb