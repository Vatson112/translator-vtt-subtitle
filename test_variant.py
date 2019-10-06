import json
import requests
import os
import re
import sys


def find_files(text):
    for i in os.listdir(text):
        if i.find('.vtt') != -1 and i.find('rus_ver') == -1:
            a.append(directory + '/' + i)


def clean_file2(some_list):
    for i, stroka in enumerate(some_list):
        if re.match(r'[a-zA-z]+', stroka) and i != 0:
            response = requests.post(
                "https://translate.yandex.net/api/v1.5/tr.json/translate?key={}&lang=en-ru&text={}".format(api_key,
                                                                                                           stroka))
            some_list[i] = str(json.loads(response.text)['text']).strip('[]') + '\n'
    return some_list


def write_file(some_list):
    with open(file + 'rus_ver.vtt', 'w', encoding='utf-8') as rus_f:
        for stroka in some_list:
            rus_f.write(stroka)


api_key = 'trnsl.1.1.20191005T145417Z.b8abc2ab0937bfa5.c517dc5e20c65064175cab9a1510c9e644e1098d'
a = []
directory = sys.argv[1]
find_files(directory)

for file in a:
    with open(file, encoding='utf-8') as f:
        open_file = f.readlines()
        clean_file2(open_file)
        write_file(open_file)
        print('Done')
