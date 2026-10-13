# 숫자와 문자열
my_name = 'Python' #문자열
my_age = 25 #숫자
print(my_name, '은 이제', my_age, '살이야.')

my_next_age = my_age + 1
print('내년에는', my_next_age, '살이야.')


multiply = 9 * 9 #81
divide = 30 / 5 #6
power = 2 ** 10 #1024 (2의 10승, 거듭제곱)
reminder = 15 % 4 #3 (나머지)

print(multiply, divide, power, reminder)

text = '2015' + '1991'
number = 2015 + 1991

print(text)
print(number)

# text_minus = text - '1991' #문자열은 뺄셈이 안된다. => TypeError: unsupported operand type(s) for -: 'str' and 'str' 발생❌