import csv

results = {}

with open('지출내역_데이터.csv', 'r', encoding='utf-8-sig') as file:
    contents = csv.DictReader(file)

    
    for content in contents:
        item = content['분류']
        price = int(content['금액'])
        
        if item not in results:
            results[item] = price
        else:
            results[item] += price

    print(results)

