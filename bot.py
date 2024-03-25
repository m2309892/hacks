import telebot
from langchain.chat_models.gigachat import GigaChat
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from telebot.types import ReplyKeyboardRemove

# import requests

# url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

# payload='scope=GIGACHAT_API_PERS'
# headers = {
#   'Content-Type': 'application/x-www-form-urlencoded',
#   'Accept': 'application/json',
#   'RqUID': 'идентификатор_запроса',
#   'Authorization': 'Basic <авторизацонные_данные>'
# }

# response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)

user_data = []

# # # token = '74c44c3e-8bf0-4ad6-9140-11ba5035e094'
sber = 'NzRjNDRjM2UtOGJmMC00YWQ2LTkxNDAtMTFiYTUwMzVlMDk0OmFhNTVjY2E1LTAwMmMtNGY3OC1hMWI5LTg0ZTYxYjU5YjkyZg=='

TOKEN = '7099603739:AAHp-mlp_amzo2cbSfvlmv4SEST4TjxwHyI'
bot = telebot.TeleBot(TOKEN)
# from random import randint

user_conversations = {}
# Функция, которую вы хотите вызвать при получении текстового сообщения
# def call_my_llm(message):
    # return chat(message)
llm = GigaChat(credentials=sber, verify_ssl_certs=False)
conversation = ConversationChain(llm=llm, verbose=True, memory=ConversationBufferMemory())
@bot.message_handler(content_types=['audio',
                                    'video',
                                    'document',
                                    'photo',
                                    'sticker',
                                    'voice',
                                    'location',
                                    'contact'])
def not_text(message):
    bot.send_message('К сожалению, я работаю только с текстовыми сообщениями')

@bot.message_handler(commands=['start'])
def handle_test_message(message):
    user_id = message.chat.id
    user_conversations[user_id] = ConversationBufferMemory()
    conversation.memory = user_conversations[user_id]
    response = conversation.predict(input=message.text)
    result = conversation.memory.chat_memory.messages[-1].content
    bot.send_message(user_id, result)
template = '''Ты менеджер-помощник в нашей комании GarageRV. Твоя задача отвечать на вопросы про автодома, и нашу компанию.\
    Мы предоставляем возможность проката в определенных городах: Москве, Нижнем Новгороде, Краснодаре. На другие вопросы отвечай\
    что не знаешь. При желании забронировать автодом спрашивай про город, даты и количество человек'''
    
conversation = ConversationChain(llm=llm,
                                verbose=True,
                                memory=ConversationBufferMemory())
conversation.prompt.template = template

conversation.prompt

# bot.message_handler(commands=['reset'])
# def handle_command(message):
#     bot.reply_to(message, "такой команды нет")

# @bot.message_handler(commands=['start'])
# def handle_command(message):
#     global user_data
#     user_data = []
#     # result = call_my_llm("Привет! Я хотел бы арендовать автодом. Скажи мне, кто ты, и спроси, куда я хочу поехать.")
#     result = "Добрый день! Я Advanced GigaChat, виртуальный ассистент. Я здесь, чтобы помочь вам определиться с арендой автодома. Подскажите, в каком регионе вы планируете совершить путешествие?"
#     bot.send_message(message.chat.id, result)

# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     if len(user_data) == 0:
#         if message.text not in ['Нижний Новгород', 'Москва', 'Краснодар']:
#             result = "Упс, кажется здесь у нас точно нет пункта проката... Выбери один из доступных городов: Москва, Нижний Новгород, Краснодар"
#         else:
#             user_data.append(message.text)
#             # result = call_my_llm(message.text + "; Теперь спроси меня, как долго я хочу провести в путешествии")
#             result = "Замечательно! Теперь, чтобы нам было легче подобрать автодом, введите даты бронирования автодома (ДД.ММ.ГГГГ - ДД.ММ.ГГГГ):"
#     elif len(user_data) == 1:
#         map = message.text.split()
#         # if len(map) < len('ДД.ММ.ГГГГ - ДД.ММ.ГГГГ') or len(map) > len('ДД.ММ.ГГГГ - ДД.ММ.ГГГГ'):
#         #     result = "Я ведь просил вводить дату в определнном формате... Введите даты бронирования автодома заново (ДД.ММ.ГГГГ - ДД.ММ.ГГГГ)"
#         # elif not (map[2] == '.' and map[5] == '.' and map[9:12] == ' - ' and map[14] == '.' and map[17] == '.' and map[0:2].is_integer and map[3:5].is_integer and map[6:10].is_integer and map[12:14].is_integer and map[15:17].is_integer and map[18:].is_integer):
#         #     result = "Я ведь просил вводить дату в определнном формате... Введите даты бронирования автодома заново (ДД.ММ.ГГГГ - ДД.ММ.ГГГГ)"
#         # else:
#         user_data.append(message.text)
#         # result = call_my_llm(message.text + "; Теперь спроси меня, с какими людьми я хочу поехать в путешествие")
#         result = "На скольких человек планируете арендовать автодом?"
        
#     elif len(user_data) >= 2:
#         user_data.append(message.text)
#         # result = call_my_llm(f"Моё место для путешествия: {user_data[0]}. Мой срок путешествия: {user_data[1]}. Мои планируемые спутники: {user_data[2]}" + "; Теперь резюмируй всю полученную информацию и скажи, что в ближайшее время мне напишет оператор.")
#         result = f"Резюмирую: \nВаше место для путешествия: {user_data[0]}; \nВаши сроки бронирования: {user_data[1]}; \nКоличество людей: {user_data[2]}.\nСпасибо за предоставленную информацию! В ближайшее время с вами свяжется наш оператор."
    
#     bot.send_message(message.chat.id, result, reply_markup=ReplyKeyboardRemove())

bot.polling(non_stop=True)