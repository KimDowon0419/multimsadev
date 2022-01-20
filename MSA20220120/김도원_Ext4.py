# 4개의 과목을 합계(전체 합계, 개인 합계) + 평균 (개인 평균 / 전체 평균)

Score1 = {"국어" :95,"영어" :90,"수학" :80,"과학" :50}
Score2 = {"국어" :100,"영어" :50,"수학" :90,"과학" :90}
Score3 = {"국어" :99,"영어" :60,"수학" :100,"과학" :40}
Score4 = {"국어" :55,"영어" :80,"수학" :80,"과학" :60}

lst = [Score1,Score2,Score3,Score4]


i = 0
total = []
while i < len(lst):
    for j in list(lst[i].values()):
        total.append(j)
    i = i + 1
t_total1 = total[:4]
t_total2 = total[4:8]
t_total3 = total[8:12]
t_total4 = total[12:]

total1 = sum(t_total1)
total2 = sum(t_total2)
total3 = sum(t_total3)
total4 = sum(t_total4)

average1 = total1 /len(t_total1)
average2 = total2 /len(t_total2)
average3 = total3 /len(t_total3)
average4 = total4 /len(t_total4)

p_total_list = [total1,total2,total3,total4]
p_average_list = [average1,average2,average3,average4]

total = sum(p_total_list)
average = sum(p_average_list)/len(p_average_list)

temp = 0

