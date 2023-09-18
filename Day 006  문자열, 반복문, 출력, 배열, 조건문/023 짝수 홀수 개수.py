def solution(num_list):
    even = 0
    odd = 0
    for i in num_list:
        odd += 1 if i % 2 else 0
            
    even = len(num_list) - odd
    
    return [even, odd]