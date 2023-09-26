def solution(array, n):
    if max(array) < n:
        return max(array)
    elif min(array) > n:
        return min(array)
    else:
        s = [i for i in array if i < n]
        b = [i for i in array if i >= n]
        if min(b) - n < n - max(s):
            return min(b)
        else:
            return max(s)