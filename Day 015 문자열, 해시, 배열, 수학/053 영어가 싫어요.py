number = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def solution(numbers):
    result = ''
    c = ''
    for s in numbers:
        c += s
        if c in number:
            result += str((number.index(c)))
            c = ''
    return int(result)