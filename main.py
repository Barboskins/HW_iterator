"""
1. Написать класс итератора, который по каждой стране из
файла countries.json ищет страницу из википедии.
Записывает в файл пару: страна – ссылка. Ссылку формировать самостоятельно.

"""
import json
from pprint import pprint
import hashlib

class SearchWiki:
    def __init__(self, name_f):
        self.name = name_f
        self.course = -1
    def __iter__(self):
        return self
    def __next__(self):
        with open(self.name, encoding='utf-8') as f:
            json_data = json.load(f)
            self.course+=1
            if self.course >= len(json_data):
              raise StopIteration
        return json_data[self.course]['name']['common']

if __name__ == '__main__':
    with open ("linkcountry.txt","w",encoding='utf-8') as file:
      for elem in SearchWiki('countries.json'):
        file.write(f"{elem} - https://ru.wikipedia.org/wiki/{elem} \n")

"""
2. Написать генератор, который принимает путь к файлу.
При каждой итерации возвращает md5 хеш каждой строки файла.
"""
import os

def md5_hush(name_file):
  way = os.path.join(os.getcwd(),name_file)
  with open (way, encoding='utf-8') as f:
    for line in f:
      yield hashlib.md5(line.encode()).hexdigest()

if __name__ == '__main__':
    for line in md5_hush('linkcountry.txt'):
      print(line)