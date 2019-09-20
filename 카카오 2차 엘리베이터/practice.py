import requests
import time
from pprint import pprint
from collections import deque

url = 'http://localhost:8000'


def start(user, problem, count):
    # uri = url + '/start' + '/' + user + '/' + str(problem) + '/' + str(count)
    uri = f'{url}/start/{user}/{problem}/{count}'
    return requests.post(uri).json()


def oncalls(token):
    uri = url + '/oncalls'
    return requests.get(uri, headers={'X-Auth-Token': token}).json()


def action(token, cmds):
    uri = url + '/action'
    return requests.post(uri, headers={'X-Auth-Token': token}, json={'commands': cmds}).json()


user = 'tester'
problem = 0
count = 4
level = 5
elv = [[0] * 5 for _ in range(count)]

ret = start(user, problem, count)

token = ret['token']

available = deque([0, 1, 2, 3])           # 사용가능한 엘리베이터 id
process = [[[], []] for _ in range(count)]  # process[i][0]: i번 엘리베이터의 올라가는 콜, process[i][1]은 내려가는 콜.