list = [1,2,3,4,5]

# 아래 세가지 방법들은 같은 결과를 나타냄
# 방법1
for i, v in enumerate(list):
    print('{}번째 값: {}'.format(i, v))

# 방법2
for a in enumerate(list):
    print('{}번째 값: {}'.format(a[0], a[1]))

# 방법3
for a in enumerate(list):
    print('{}번째 값: {}'.format(*a))

# 딕셔너리에서도 동일하게 적용이 가능함
ages = {'Tod':35, 'Jane':23, 'Paul':62}

# 방법1
for key, value in ages.items():
    print('{}의 나이:{}'.format(key, value))

# 방법2
for b in ages.items():
    print('{}의 나이:{}'.format(b[0], b[1]))

# 방법3
for b in ages.items():
    print('{}의 나이:{}'.format(*b))