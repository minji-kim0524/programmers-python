list = [1,2,3,5,7,2,5,237,55]

# break: 반복문을 종료시키는 역할
for val in list:
    if val % 3 == 0:
        print(val)
        break # 첫번째 결과값만을 반환하고 if문이 종료됨

# continue: 제외하는 경우를 첫번째에 처리함
# - 반복문의 나머지 부분을 보지않고 반복문의 처음으로 돌아간다
# 방법1
# for i in range(10):
#     if i % 2 != 0:
#         print(i)
#         print(i)
#         print(i)
#         print(i)

# 방법2
for i in range(10):
    if i % 2 == 0:
        continue # 다시 처음(for문)으로 돌아감
    print(i)
    print(i)
    print(i)
    print(i)