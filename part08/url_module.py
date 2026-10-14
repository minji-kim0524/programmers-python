# 모듈
# - 미리 만들어진 코드를 가져와 쓰는 방법
# - import <모듈이름>
# - 사용방법: <모듈이름>.<모듈안의 구성요소>
#   예) math.pi, random.choice()
def get_web(url):
    """URL을 넣으면 페이지 내용을 돌려주는 함수"""
    import urllib.request
    response = urllib.request.urlopen(url) # url을 열고
    data = response.read() # 데이터를 읽어서
    decoded = data.decode('utf-8') # 사람이 읽을 수 있게 디코딩하고
    return decoded # 반환

url = input('웹 페이지 주소를 입력하세요')
content = get_web(url)
print(content)