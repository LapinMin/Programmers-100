def solution(numbers, direction):
    result = []
    if direction == "right":
        result = [numbers[i] for i in range(-1, len(numbers)-1)]
    else:
        result = [numbers[i] for i in range(1, len(numbers))]
        result.append(numbers[0])
    return result