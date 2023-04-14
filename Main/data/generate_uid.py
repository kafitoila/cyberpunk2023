import random
import string
import csv

#  For test
def test_filter():
    # uid_in_use = ['BCDEFG','HIJKLM']
    uid = ['ABCDEF','BCDEFG','GHIJKL','HIJKLM','MNOPRS','TUVWYZ','012345','678901','234567','891234',
    'STIMXX','DRFXXX','MNOGOX','N0LIKI','KRESTI','POISK0','TAINAS','KUCKLI','TRAVAK','BREZEN',
    'KULEKK','DYMDYM','OKOKOK','NANANA','QWEQWE','QWE123','RTY456','678UIP','912ASD','4FH7G5']
    test_uid: list = []
    while len(uid) > 0:
        id = filter_out(uid, ous)
        test_uid.append(id)
    print(test_uid)

alphabet = string.ascii_uppercase + string.digits
alpha_safe = alphabet.replace('0','').replace('O','')    # Exclude 0 and O
uid_length: int = 6
drugs = {'A', 'S', 'D'}
zero = {'0'}
ous = {'0','O'}

def random_choice():
    return ''.join(random.choices(alpha_safe, k=uid_length))
def random_choice_num():
    return ''.join(random.choices(string.digits, k=uid_length))

def generate_uid(function, uid_in_use) -> list:
    out = []
    count = 0
    for _ in range(12000):
        new = function()
        if new not in out and new not in uid_in_use and new.isdigit() == False:
            out.append(new)
    return out

def filter_first_char(uid: list, reserved) -> str:
    id = uid.pop()
    if id[0] in reserved:
        print(id)
        id = filter_first_char(uid, reserved)
    return id

def filter_first_char_reversed(uid: list, reserved) -> str:
    id = uid.pop()
    try:
        if id[0] not in reserved:
            id = filter_first_char_reversed(uid, reserved)
    except:
        exit
    return id

def filter_out(uid: list, banned) -> str:
    id = uid.pop()
    for c in id:
        if c in banned:
            print(c,': ',id)
            id = filter_out(uid, banned)
            break
    return id

def add_uid_name(from_file,to_file):
    with open(from_file,'r', encoding='UTF8', newline='') as ff:
        reader = csv.reader(ff)
        with open(to_file,'w', encoding='UTF8', newline='') as tf:
            writer = csv.writer(tf)
            for row in reader:
                user_id = filter_first_char(uid_num, zero)
                secret_id = filter_first_char(uid, drugs)
                wrt = [row[0], user_id, secret_id]
                # print(wrt)
                writer.writerow(wrt)

def add_uid_implant_general(from_file,to_file,page_count):
    with open(from_file,'r', encoding='UTF8', newline='') as ff:
        reader = csv.reader(ff)
        with open(to_file,'w', encoding='UTF8', newline='') as tf:
            writer = csv.writer(tf)
            data: list = []
            data.extend(reader)
            for page in range(page_count):
                page_name = [f'Page {page + 1}']
                writer.writerow(page_name)
                print(len(data))
                for row in data:
                    id = filter_first_char(uid, drugs)
                    wrt = [row[0], id]
                    writer.writerow(wrt)
                print(len(data))
                writer.writerow('')

def add_uid_implant_additional(from_file,to_file,row_count):
    with open(from_file,'r', encoding='UTF8', newline='') as ff:
        reader = csv.reader(ff)
        with open(to_file,'a', encoding='UTF8', newline='') as tf: # 'a' - append
            writer = csv.writer(tf)
            data: list = []
            data.extend(reader)
            for row in data:
                writer.writerow(row)
                for page in range(row_count):
                    id = filter_first_char(uid, drugs)
                    wrt = [id]
                    writer.writerow(wrt)
                writer.writerow('')

def add_uid_terminal(from_file,to_file,row_count):
    with open(from_file,'r', encoding='UTF8', newline='') as ff:
        reader = csv.reader(ff)
        with open(to_file,'w', encoding='UTF8', newline='') as tf:
            writer = csv.writer(tf)
            data: list = []
            data.extend(reader)
            for row in data:
                writer.writerow(row)
                for page in range(row_count):
                    wrt = []
                    for r in row:
                        id = filter_first_char(uid, drugs)
                        wrt.append(id)
                    writer.writerow(wrt)
                writer.writerow('')


def add_uid_medicine(to_file,column_count,row_count,page_count):
    with open(to_file,'w', encoding='UTF8', newline='') as tf:
        writer = csv.writer(tf)
        for page in range(page_count):
            for row in range(row_count):
                wrt = []
                for column in range(column_count):
                    id = filter_first_char_reversed(uid, drugs)
                    wrt.append(id)
                writer.writerow(wrt)
            writer.writerow('')

def add_uid_secret_id(to_file,column_count,row_count,page_count):
    with open(to_file,'w', encoding='UTF8', newline='') as tf:
        writer = csv.writer(tf)
        for page in range(page_count):
            for row in range(row_count):
                wrt = []
                for column in range(column_count):
                    id = filter_first_char(uid, drugs)
                    wrt.append(id)
                writer.writerow(wrt)
            # writer.writerow('')

def transpose_data(from_file,to_file):
    with open(from_file,'r', encoding='CP1251', newline='') as ff:
        reader = csv.reader(ff)
        with open(to_file,'w', encoding='UTF8', newline='') as tf:
            writer = csv.writer(tf)
            for row in reader:
                for r in row:
                    if r != row[0] and r != '':
                        id = filter_first_char(uid, drugs)
                        wrt = [row[0], r, id]
                        writer.writerow(wrt)

def correct_uid(from_file,to_file):
    with open(from_file,'r', encoding='UTF8', newline='') as ff:
        reader = csv.reader(ff)
        with open(to_file,'w', encoding='UTF8', newline='') as tf:
            writer = csv.writer(tf)
            for row in reader:
                if row[2].find('0') > -1 or row[2].find('O') > -1:
                    print(row)
                    row[2] = filter(uid, drugs)
                    wrt = [row[0], row[1], row[2], '  <-- here']
                else:
                    wrt = [row[0], row[1], row[2]]
                # print(wrt)
                writer.writerow(wrt)

def load_model(from_file):
    data: list = []
    with open(from_file,'r', encoding='UTF8', newline='') as ff:
        reader = csv.reader(ff)
        data.extend(reader)
    return data

def get_uid(model,col) -> list:
    uid: list = []
    for line in model:
        try:
            uid.append(line[col])
        except IndexError:
            pass
    return uid

def get_collisions(uid_in_use) -> int:
    collision_count = 0
    for id in uid_in_use:
        if uid_in_use.count(id) != 1:
            collision_count += 1
            print(id)
    return collision_count


name_model = load_model('users.csv')
uid_in_use = get_uid(name_model,2)
implant_model = load_model('implants.csv')
uid_in_use.extend(get_uid(implant_model,1))
implant_start_model = load_model('implants_start.csv')
uid_in_use.extend(get_uid(implant_start_model,2))
terminal_model = load_model('terminal_print.csv')
uid_in_use.extend(get_uid(terminal_model,0))
uid_in_use.extend(get_uid(terminal_model,1))
uid_in_use.extend(get_uid(terminal_model,2))
uid_in_use.extend(get_uid(terminal_model,3))
uid_in_use.extend(get_uid(terminal_model,4))
uid_in_use.extend(get_uid(terminal_model,5))
print(len(uid_in_use))
print(get_collisions(uid_in_use))

uid = generate_uid(random_choice, uid_in_use)
# uid_num = generate_uid(random_choice_num, uid_in_use)

# add_uid_terminal('terminal_template.csv','terminal_print.csv',20)
# add_uid_medicine('medicine_print.csv',9,39,3)

add_uid_secret_id('secret_id_print.csv',9,39,3)