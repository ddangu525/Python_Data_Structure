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


class Elevator:
    def __init__(self, id, floor, status, passengers, level):
        self.id = id
        self.floor = floor
        self.status = status
        self.passengers = passengers
        self.level = level

    def up(self):
        if self.floor == self.level:
            return
        self.floor += 1

    def down(self):
        if self.floor == 1:
            return
        self.floor -= 1

    def open(self):
        self.status = 'OPENED'

    def close(self):
        self.status = 'CLOSED'

    def stop(self):
        self.status = 'STOPPED'

    def enter(self, passengers):
        self.passengers.extend(passengers)

    def exit(self, passengers):
        pass


user = 'tester'
problem = 0
count = 4
level = 5
elv = [[0] * 5 for _ in range(count)]

ret = start(user, problem, count)

token = ret['token']

oncall = oncalls(token)
pprint(oncall)
calls = oncall['calls']
pprint(calls)

upcalls = deque()
downcalls = deque()
while calls:
    call = calls.pop()
    if call['start'] < call['end']:
        upcalls.append((call['start'], call['end'], call['id']))
    else:
        downcalls.append((call['start'], call['end'], call['id']))
print(f'upcall = {upcalls}\ndowncall = {downcalls}')
elevators = []
available = set()
for ele in oncall['elevators']:
    # 현재층, 탑승자, 상태, 내 정의 상태..4가지. 0이면 stop 1 2 3 4 각 4가지 상태, 뒤에는 태우러 가는지 내려주러 가는지.
    elevators.append([ele['floor'], ele['passengers'], ele['status'], 0, 0])
    if not ele['passengers'] and ele['status'] == 'STOPPED':
        available.add((ele['id'], ele['floor']))
print('elevators', elevators)
print('available:', available)

for call in upcalls:
    if available:
        ele = min(available, key=lambda x: abs(x[1] - call[0]))
        available.discard(ele)
        print(ele)

for call in downcalls:
    if available:
        ele = min(available, key=lambda x: abs(x[1] - call[0]))
        available.discard(ele)
        print(ele)


# 각 층에서 위로 가려고 누른 요청.. 아이디랑, 층을 저장해야겠지?? 얘를 우선순위 큐로 구현..?
# # 레퍼런스 지정을 위해 elevator 클래스 구현??
# upcalls = [[] for _ in range(level + 1)]
# # 각 층에서 아래로 가려고 누른 요청.
# dncalls = [[] for _ in range(level + 1)]
#
# for call in calls:
#     if call['start'] < call['end']:
#         upcalls[call['start']].append((call['id'], call['end']))
#     else:
#         dncalls[call['start']].append((call['id'], call['end']))

cmds = []
# for
# 최종적으로는 이런식으로 구현..초당 40회가 넘지 안도록 시간 제한도 걸어줘야 할듯..
# 루프 하나당 2번 api 호출되니까.. 끝에 0.05초정도 sleep 해주기.(문제 되는 게 확인되면)
# 일단 우리가 타는 엘레베이터 처럼 구현해보자.. 올라가는도중에 누르면 태워서 같이 올라가고.. 내려가는거 누르면 기다리게 하고..
# 그 다음에 여러 대를 어떻게 운영할지 고민.. 노는 엘베는 중간층에다 놔두면 콜 들어왔을 때 이동이 빠르지 않을까?
# 여기서 문제에 맞는 휴리스틱을 사용...
# while 1:
#     oncall = oncalls(token)
#     if oncall['is_end']:
#         break
