dic = {
    "zero" : 0, "one" : 1, "two" : 2,
    "three" : 3, "four" : 4, "five" : 5,
    "six" : 6, "seven" : 7, "eight" : 8,
    "nine" : 9
}

def solution(numbers):
    answer = ""
    buff = ""
    
    for i in numbers:
        buff += i
        number = dic.get(buff)
        if number != None:
            answer += str(number)
            buff = ""
            
    return int(answer)
