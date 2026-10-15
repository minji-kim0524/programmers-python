# packing, unpacking
# - packing: 하나의 변수에 여러개의 값을 넣음
# - unpacking: 변수에서 여러개의 값을 꺼내옴

# c의 값을 unpacking 해서 d,e에 넣은 상황
c = (3, 4)
d, e = c
print(d) # 3
print(e) # 4

# d, e를 f에 packing 한 상황
f = d, e
print(f) # (3, 4)


# tuple을 사용하면 함수의 리턴값으로 여러 값을 전달할 수 있음
def tuple_func():
    return 1, 2

q, w = tuple_func()
print(q, w) # 1 2