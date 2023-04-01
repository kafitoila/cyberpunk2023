menu_start = 'Регистрация'
start = 'Для регистрации введите команду формата /start ХХХХХХ, где ХХХХХХ - выданный вам код'
menu_pay = 'Перевод денег'
pay = 'Перевод денег'
menu_balance = 'Текущий баланс'
balance = 'Текущий баланс'
menu_pay_from = 'Перевод от организации'
pay_from = 'Перевод от организации'
menu_set_access = 'Выдать доступ к счету организации'
set_access = 'Выдать доступ к счету организации'
menu_get_access = 'Просмотр доступов к счёту организации'
get_access = 'Просмотр доступов к счёту организации'

menu_help = 'Список команд'
help = f'/help - {menu_help}\n' \
f'/start - {menu_start}\n' \
f'{start}\n\n' \
f'/pay - {menu_pay}\n' \
f'/balance - {menu_balance}\n' \
f'/pay_from - {menu_pay_from}\n' \
f'/set_access - {menu_set_access}\n' \
f'/get_access - {menu_get_access}\n'
default = 'Команда не распознана. Проверьте правильность написания'

comm: dict[str, str] = {
                '/command_1': 'command_1 desription',
                '/command_2': 'command_2 desription',
                '/command_3': 'command_3 desription',
                '/command_4': 'command_4 desription'}