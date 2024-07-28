n = input()  # 과목의 수 입력 
# 공백으로 구분된 정수 형태로 입력된 과목 점수를 정수형으로 리스트에 저장
mylist = list(map(int, input().split()))  
mymax = max(mylist)  # 최고점 계산 
sum = sum(mylist)  # 총합 계산
print(sum * 100 / mymax / int(n))
