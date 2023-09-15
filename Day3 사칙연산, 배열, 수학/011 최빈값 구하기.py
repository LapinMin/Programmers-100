def solution(array):
    a = [0 for _ in range(max(array)+1)]
    
    for i in array:
        a[i] += 1
    
    cnt = max(a)
    
    if a.count(cnt) == 1:
        return a.index(cnt)
    else:
        return -1
