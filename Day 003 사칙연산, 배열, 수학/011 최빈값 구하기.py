def solution(array):
    count = [0] * (max(array) + 1) # array 안의 각 수들의 등장 횟수를 세기 위해 배열 안 최대수 + 1만큼의 배열 생성
    
    for i in array:
        count[i] += 1 # array 로 반복문 돌려 count 배열의 해당 인덱스 자리에 1씩 추가
            
    mode = 0 # 최빈수 개수 구하기 위한 변수
            
    for c in count:
        if c == max(count):
            mode += 1
    
    return count.index(max(count)) if mode == 1 else -1 # 배열.index(값) => 배열 안에 해당 값의 index 구하는 방법

    #count.count(max(count)) 로 최빈값 개수 구할 수 있음