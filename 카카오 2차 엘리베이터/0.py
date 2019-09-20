import requests
import time
from pprint import pprint
from collections import deque

url = 'http://localhost:8000'


def start(user, problem, count):
    uri = f'{url}/start/{user}/{problem}/{count}'
    return requests.post(uri).json()


def oncalls(token):
    uri = url + '/oncalls'
    return requests.get(uri, headers={'X-Auth-Token': token}).json()


def action(token, cmds):
    uri = url + '/action'
    return requests.post(uri, headers={'X-Auth-Token': token}, json={'commands': cmds}).json()


# 1. 시작. token 받아오기.
user = 'tester'
problem = 0
count = 4
level = 5
elv = [[0] * 5 for _ in range(count)]

ret = start(user, problem, count)

token = ret['token']

# 2. 동작 시뮬레이션
while 1:
    # 2-1 현재 상태 받아오기
    oncall = oncalls(token)
    # 종료 조건 확인
    if oncall['is_end']:
        break
    # 정보 업데이트

    cmds = []
    # 2-2 알고리즘에 따라 액션 해주기.
    action(token, cmds)
