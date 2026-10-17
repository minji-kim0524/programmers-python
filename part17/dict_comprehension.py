# 딕셔너리 컴프리헨션 (Dictionary Comprehension) 
students = ['태연','진우','정현','하늘','성진']

for number, name in enumerate(students):
    print('{}번의 이름은 {}입니다.'.format(number, name))

students_dict = {'{}번'.format(number+1): name for number, name in enumerate(students)}
print(students_dict) # {'1번': '태연', '2번': '진우', '3번': '정현', '4번': '하늘', '5번': '성진'}

# zip 활용법
# - zip은 두 개 이상의 리스트나 스트링을 받아서 인덱스에 맞게 자료를 묶어주는 역할을 함
scores = [85, 92, 78, 90, 100]

for x, y in zip(students, scores):
    print(x, y)

# Dictionary Comprehension
score_dic = {student: score for student, score in zip(students, scores)}
print(score_dic)