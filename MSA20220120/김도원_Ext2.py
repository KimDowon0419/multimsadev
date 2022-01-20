# 4개의 과목을 합계(전체 합계, 개인 합계) + 평균 (개인 평균 / 전체 평균)

Score1 = {"국어" :95,"영어" :90,"수학" :80,"과학" :50}
Score2 = {"국어" :100,"영어" :50,"수학" :90,"과학" :90}
Score3 = {"국어" :99,"영어" :60,"수학" :100,"과학" :40}
Score4 = {"국어" :55,"영어" :80,"수학" :80,"과학" :60}

list = [Score1,Score2,Score3,Score4]
p_total_list = []
p_average_list = []
i = 0
while i < len(list): 
    Score = list[i].values()
    t = sum(Score)
    p_total_list.append(t)
    p_average_list.append(t/len(list))
    i = i + 1

total= sum(p_total_list)
average = sum(p_average_list)/len(p_average_list)

temp = 0