def solution(num_list, n):
    result = []
    for i in range(0, len(num_list), n):
        part = []
        for j in range(i, i + n):
            part.append(num_list[j])
        result.append(part)
    return result