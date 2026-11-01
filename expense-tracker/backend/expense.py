# 파일 분석 로직 작성
import csv

def analyze_expense_file(file):
    results = {}

    # 1. 파일을 읽고
    contents = csv.DictReader(file)

    # 2. 각 항목별 금액을 더하고
    for content in contents:
        item = content['분류']
        price = int(content['금액'])
        
        if item not in results:
            results[item] = price
        else:
            results[item] += price

    # 3. 결과를 반환
    return results