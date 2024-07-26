n = input()  # 숫자의 개수 입력 받기
numbers = list(input())  # 숫자 n개 입력 받기
sum = 0   # 변수 선언

for i in numbers:  # numbers 리스트에 저장된 각 자릿수를
    sum += int(i)  # 정수형으로 변환 후 합함
print(sum)  # 결과 출력 