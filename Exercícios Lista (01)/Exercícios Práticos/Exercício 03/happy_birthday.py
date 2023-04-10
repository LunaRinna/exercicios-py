__author__ = "Luna Antunes"

import json

friends = open('friends_list.json', encoding='utf-8')
data = json.load(friends)
isBirthday = False

def func_is_birthday(any_date):
    global isBirthday
    for friend in data['my_friends']:
        print("Name:", friend['name'])
        print("Surname:", friend['surname'])
        print("Email:", friend['email'])
        print("Birthday:", friend['birthday'])
        print()
        if (friend['birthday']) == any_date:
            isBirthday = True
            print("Today is the birthday of", friend['name'], friend['surname'], "\nSending birthday e-mail to the registered e-mail:", friend['email'],"\n")
            continue
        else:
            continue
    return isBirthday

