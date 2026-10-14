
for i in [0, 1, 2, 3, 4]:
    print(i)

for i in range(5): # 1이 아닌 0부터 시작됨
    print(i)

names = ['철수', '영희', '바둑이', '귀도', '비단뱀']

for i in range(len(names)):
    name = names[i]
    print('{}번: {}'.format(i + 1, name))

# enumerate: 한번에 순서와 값을 모두 만들어냄
for i, name in enumerate(names):
    print('{}번: {}'.format(i + 1, name))

# list 와 range 의 차이
# - for in list: 순회할 리스트가 정해져 있을 때
# - for in range(): 순회할 횟수가 정해져 있을 때