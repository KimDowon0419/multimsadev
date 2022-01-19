#1 딕셔너리를 이용해서 평군 점수 구하기
Score = {"국어" :95,"영어" :90,"수학" :80,"과학" :50}
average = sum(Score.values())/len(Score.values())

#2 셋을 이용해서 1~100 까지 숫자 중에 공배수를 구함 : 5의 공배수만 구하기
# : 표현식을 이용하면 쉽다.
setdata5 = {i for i in range(1,101) if i % 5 == 0}  

#3 #2의 결과를 이용해서 3의 공배수를 구하고 2의 결과 3의 결과의 합집합
setdata3 = {i for i in range(1,101) if i % 3 == 0}
resultData = setdata5 | setdata3  

#4 리스트 데이터 : 7,5,3,1,-1,-3,-5,-7 출력 : range 활용할것
lst = []
for data in range(7,-9,-2):
    lst.append(data)

print (lst)

#5 #4의 결과를 튜플로 변경(형변환)
tuple = tuple(lst)

#디버깅용
temp = 1
