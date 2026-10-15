# 에러를 직접 발생시켜보기

# 예시1
# def rsp(mine, yours):
#     #가위바위보 승패를 판단하는 함수
#     allowed = ['가위', '바위', '보']
#     if mine not in allowed:
#         raise ValueError
#     if yours not in allowed:
#         raise ValueError

# try:
#     rsp('가위', '바')
# except ValueError:
#     print('잘못된 값을 입력하였습니다.')

# 예시2
school = {'1반':[172, 185, 198, 177, 165, 199], '2반':[165, 177, 167, 180, 191]}

try:
    for class_number, students in school.items(): # 1번째 for문
        for student in students: # 2번째 for문
            if student > 190:
                print(class_number,'반에 190을 넘는 학생이 있습니다.')
                # break # 2번째 for문만 끝냄 -> 첫번째 결과값만 나오고 종료 시키고 싶다면 raise사용
                raise StopIteration
except StopIteration:
    print('정상종료')