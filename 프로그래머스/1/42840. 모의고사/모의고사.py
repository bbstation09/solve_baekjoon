def solution(answers):
    answer = []
    
    stu_1 = [1,2,3,4,5]
    stu_2 = [2,1,2,3,2,4,2,5]
    stu_3 = [3,3,1,1,2,2,4,4,5,5]
    
    score_1, score_2, score_3 = 0, 0, 0
    
    for i in range(len(answers)):
        if answers[i] == stu_1[i % len(stu_1)]: score_1 += 1
        if answers[i] == stu_2[i % len(stu_2)]: score_2 += 1
        if answers[i] == stu_3[i % len(stu_3)]: score_3 += 1
        
    score = [score_1, score_2, score_3]    
    max_score = max(score_1, score_2, score_3)
    
    for i in range(3):
        if max_score == score[i]:
            answer.append(i+1)
    
    answer.sort()
    return answer