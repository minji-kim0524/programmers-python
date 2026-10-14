
def root(a, b, c): # a, b, c는 매개변수(parameter) 
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

    return r1, r2 # 여러값을 반환하려면 return 뒤에 쉼표로 구분하여 나열하면 됨

x = 1
y = 2
z = -8

r1, r2 = root(x, y, z)
print('근은 {} {}'.format(r1, r2))
