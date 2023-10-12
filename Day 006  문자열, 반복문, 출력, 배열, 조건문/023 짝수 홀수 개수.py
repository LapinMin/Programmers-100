def solution(num_list):
    even = 0
    odd = 0
    for i in num_list:
        odd += 1 if i % 2 else 0
            
    even = len(num_list) - odd
    
    return [even, odd]

    # 3항연산자는 꼭 써야할 경우가 아니라면 안 써도 됨. 그냥 평범하게 if-else 문으로 계산해도 충분함