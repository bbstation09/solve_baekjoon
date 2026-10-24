
def solution(brown, yellow):
    answer = []
    
    total = brown + yellow 
    
    # 가능한 가로 길이 개수 확인
    for h in range(3, int(total**0.5)+1):
        if total % h != 0: continue
    
        # 노란색 칸 개수 확인
        w = total // h
        if (w-2) * (h-2) == yellow: 
            answer.append(w)
            answer.append(h)
    
    return answer