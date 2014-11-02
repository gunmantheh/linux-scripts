#!python3.4
__author__ = 'Pavel'

import json
from urllib.request import urlopen
import ctypes
from colorama import Fore, Back, Style, init
import os, sys, time

server = '__ip__'
port = '__port__'
apikey = '__apikey__'

class Messenger:
    def __init__(self, **kwargs):
        self.__dict__ = kwargs


def loadData():
    jsonurl = urlopen('http://'+server+':'+port+'/sabnzbd/api?apikey='+apikey+'&mode=queue&output=json')
    data = jsonurl.read().decode('utf-8')
    text = json.loads(data) # <-- read from it
    return text


def printElement(elem):
    obj = Messenger(filename=str(elem['filename']), percentage=int(elem['percentage']), category=elem['cat'])
    print('['+obj.category+'] ',end='')
    print(obj.filename)
    print('%02d'%obj.percentage,end='')
    print('% [',end="")
    for i in range(20):
        if obj.percentage/5 >= i and not obj.percentage == 0:
            print(Fore.GREEN + '*',end="")
        else:
            print(' ',end="")
    print("]")


def clearScreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def setTitle(title):
    if os.name == 'nt':
        os.system('title ' + title)
    else:
        sys.stdout.write('\x1b]2;'+title+'\x07')

def main():
    init(autoreset=True) # colorama init
    while True:
        queue = loadData()['queue']
        clearScreen()
        speed = queue['speed']
        slots = queue['slots']
        if len(queue['slots']) > 0:
            setTitle('['+ speed + '/s] - ' + slots[0]['filename'] + ' - ' + slots[0]['sizeleft'])
        else:
            setTitle('Nothing is being downloaded')
        if len(slots) > 0:
            for elem in slots:
                printElement(elem)
        else:
            print(Fore.RED + "Nothins is being downloaded")
        time.sleep(5)
if __name__ == '__main__':
    main()