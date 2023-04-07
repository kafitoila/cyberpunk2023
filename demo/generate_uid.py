import random
import string
import csv

alphabet = string.ascii_uppercase + string.digits
alpha_safe = alphabet.replace('0','').replace('O','')
uid_length: int = 6
drugs = {'A', 'S', 'D'}
zero = {'0'}
ous = {'0','O'}

def random_choice():
    return ''.join(random.choices(alpha_safe, k=uid_length))
def random_choice_num():
    return ''.join(random.choices(string.digits, k=uid_length))

def generate_uid(function) -> list:
    out = []
    count = 0
    for _ in range(500):
        new = function()
        if new not in out:
            out.append(new)
    return out

uid = generate_uid(random_choice)
uid_num = generate_uid(random_choice_num)

def filter(uid: list, reserved) -> str:
    id = uid.pop()
    if id[0] in reserved:
        print(id)
        id = filter(uid, reserved)
    return id

def add_uid_name(from_file,to_file):
    with open(from_file,'r', encoding='UTF8', newline='') as ff:
        reader = csv.reader(ff)
        with open(to_file,'w', encoding='UTF8', newline='') as tf:
            writer = csv.writer(tf)
            for row in reader:
                user_id = filter(uid_num, zero)
                secret_id = filter(uid, drugs)
                wrt = [row[0], user_id, secret_id]
                # print(wrt)
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

def load_name_model(from_file):
    data: list = []
    with open(from_file,'r', encoding='UTF8', newline='') as ff:
        reader = csv.reader(ff)
        data.extend(reader)
    return data

def get_uid(model,col) -> list:
    uid: list = []
    for line in model:
        uid.append(line[col])
    return uid

def get_collisions(uid_in_use) -> int:
    collision_count = 0
    for id in uid_in_use:
        if uid_in_use.count(id) != 1:
            collision_count += 1
            print(id)
    return collision_count


# add_uid_name('user.csv','user_w_code.csv')
# correct_uid('user_full.csv','user_full_new.csv')
name_model = load_name_model('user_full.csv')
uid_in_use = get_uid(name_model,2)
collision_count = get_collisions(uid_in_use)
print(f'Collisions found: {collision_count}')