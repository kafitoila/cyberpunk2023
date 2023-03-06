from dataclasses import dataclass
import requests
import time

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

send = '/sendMessage'
sendPhoto = '/sendPhoto'
#chat_id = '499598131'
#user_name = '\u041a\u043e\u0441\u0438\u043b \u041a\u043e\u0441\u043e\u0439'

cat_url: str = 'https://aws.random.cat/meow'
cat_error_text: str = 'Нет котика('

offset: int = -2
timeout = 160
cat_response: requests.Response
cat_link: str
msg: str = ''
updates: dict

def send_cat() -> str:
    print (result)
    if 'message' in result:
        chat_id = result['message']['from']['id']
        msg = result['message']['text']
        user_name = result['message']['from']['first_name']
    else:
        chat_id = result['edited_message']['from']['id']
        msg = result['edited_message']['text']
    #res = requests.get(f'{api_url}{token}{send}?chat_id={chat_id}&text={text}')\
    if msg.startswith('/sos'):
        address = msg.strip('/sos ')
        if address != '':
            text = f'Привет, {user_name}! Травма Тим скоро прибудет в {address}.'
        else:
            text = f'Привет, {user_name}! Травма Тим скоро прибудет.'
        query = f'?chat_id={chat_id}&text={text}'
        res = requests.get(f'{api_url}{token}{send}{query}')

    else:
        text2 = f'Ого, {msg}? Ха-ха!'
        print(text2)
        query2 = f'?chat_id={chat_id}&text={text2}'
        res = requests.get(f'{api_url}{token}{send}{query2}')
        cat_response = requests.get(f'{cat_url}')
        if cat_response.status_code == 200:
            cat_link = cat_response.json()['file']
            cat_query = f'?chat_id={chat_id}&photo={cat_link}'
            requests.get(f'{api_url}{token}{sendPhoto}{cat_query}')
        else:
            requests.get(f'{api_url}{token}{send}{cat_error_text}')
    return msg

while msg != 'terminate':
    start_time = time.time()
    updates = requests.get(f'{api_url}{token}{upd}?offset={offset + 1}&timeout = {timeout}').json()
    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            print(offset)
            msg = send_cat()

    end_time = time.time()
    print (start_time - end_time)
