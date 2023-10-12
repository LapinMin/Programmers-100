gather = ['a', 'e', 'i', 'o', 'u']

def solution(my_string):
    result = ''
    for i in range(len(my_string)):
        if not my_string[i] in gather:
            result += my_string[i]
    return result