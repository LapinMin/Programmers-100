def solution(emergency):
    a = emergency.copy()
    a.sort(reverse=True)
    result = [1] * len(emergency)
    for i in range(0, len(a)):
        for j in range(0, len(a)):
            if a[i] == emergency[j]:
                result[j] += i
                break
    return result