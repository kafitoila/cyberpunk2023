def mixit(word:str, number:int=3) -> str:
    word = word.title() + ' '
    return word * number

print (mixit('python'))
#print (mixit.__annotations__)

import requests

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
token = '' #config.main_bot.token
json = '?offset={offset + 1}'
url = api_url + token
upd = '/getUpdates'
me = '/getMe'
#request(api_url+token+upd)
#request(api_url+token+me)

result = get_request_result(url + me + json)
#request_print(url + me + json)

send = '/sendMessage'
chat_id = '499598131'
user_name = '\u041a\u043e\u0441\u0438\u043b \u041a\u043e\u0441\u043e\u0439'
text = 'Привет, ' + user_name + '! Травма Тим скоро прибудет.'
text2 = 'Привет! Травма Тим скоро прибудет.'
query = '?chat_id=' + chat_id + '&text=' + text
#request_print(url + send + query)
