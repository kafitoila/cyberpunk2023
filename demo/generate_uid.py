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
    for _ in range(2000):
        new = function()
        if new not in out and new not in uid_in_use:
            out.append(new)
    return out

def filter_first_char(uid: list, reserved) -> str:
    id = uid.pop()
    if id[0] in reserved:
        print(id)
        id = filter_first_char(uid, reserved)
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
                    # print(wrt)
                    writer.writerow(wrt)
                print(len(data))
                writer.writerow('')

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


name_model = load_model('user_full.csv')
uid_in_use = get_uid(name_model,2)
implant_model = load_model('implant_print_general.csv')
uid_in_use.extend(get_uid(implant_model,1))
print(len(uid_in_use))

uid = generate_uid(random_choice, uid_in_use)
uid_num = generate_uid(random_choice_num, uid_in_use)

# add_uid_implant_general('implant_print_set.csv', 'implant_print_general.csv', 12)

transpose_data('implant_print_start.csv', 'implant_print_start1.csv')
implant_start_model = load_model('implant_print_start1.csv')
uid_in_use.extend(get_uid(implant_start_model,2))
print(len(uid_in_use))
print(get_collisions(uid_in_use))