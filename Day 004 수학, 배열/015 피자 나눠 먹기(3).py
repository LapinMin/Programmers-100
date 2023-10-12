def solution(slice, n):
    if n % slice == 0:
        return n // slice
    else:
        return (n // slice) + 1
    
    # return (n // slice) + 1 if n % slice else n // slice 로 코드 축약 가능