from dataclasses import dataclass
import requests

@dataclass
class DatabaseConfig:
    db_host: str       # URL-адрес базы данных
    db_user: str       # Username пользователя базы данных
    db_password: str   # Пароль к базе данных
    database: str      # Название базы данных

@dataclass
class MainBot:
    token: str             # Токен для доступа к телеграм-боту
    admin_ids: list[str]   # Список id администраторов бота

@dataclass
class Config:
    main_bot: MainBot
    db: DatabaseConfig

config = Config(main_bot=MainBot(token='5665289787:AAHVqrTkOvkxMpJuylPtjwy7AXAGEq96r3g',
                                 admin_ids=['id1','id2']),
                db=DatabaseConfig(db_host='DB_HOST',
                                  db_user='DB_USER',
                                  db_password='DB_PASSWORD',
                                  database='DATABASE'))

def request_print(url:str) -> None:
    response = requests.get(url)  # Отправляем GET-запрос и сохраняем ответ в переменной response

    if response.status_code == 200:    # Если код ответа на запрос - 200, то смотрим, что пришло в ответе
        print(response.json() )
    else:
        print(response.status_code)

def get_request_result(url:str) -> str | dict:
    response = requests.get(url)    # Отправляем GET-запрос и сохраняем ответ в переменной response

    if response.status_code == 200:    # Если код ответа на запрос - 200, то смотрим, что пришло в ответе
        return response.json()
    else:
        return response.status_code


api_url = 'https://api.telegram.org/bot'
token = config.main_bot.token
json = '?offset={offset + 1}'
url = api_url + token
upd = '/getUpdates'
me = '/getMe'
#request(api_url+token+upd)
#request(api_url+token+me)

#result = get_request_result(url + me + json)
#request_print(url + me + json)

offset: int = -2
updates = requests.get(f'{api_url}{token}{upd}?offset={offset + 1}').json()

send = '/sendMessage'
#chat_id = '499598131'
#user_name = '\u041a\u043e\u0441\u0438\u043b \u041a\u043e\u0441\u043e\u0439'

if updates['result']:
    for result in updates['result']:
        print (result)
        offset = result['update_id']
        chat_id = result['message']['from']['id']
        user_name = result['message']['from']['first_name']
        text = f'Привет, {user_name}! Травма Тим скоро прибудет.'
        query = f'?chat_id={chat_id}&text={text}'
        #res = requests.get(f'{api_url}{token}{send}?chat_id={chat_id}&text={text}')
        res = requests.get(f'{api_url}{token}{send}{query}')

        if result['message']['text']: msg = result['message']['text']
        text2 = f'Ого, {msg}? Ха-ха!'
        print(text2)
        query2 = f'?chat_id={chat_id}&text={text2}'
        res = requests.get(f'{api_url}{token}{send}{query2}')
