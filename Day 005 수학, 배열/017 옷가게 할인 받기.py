def solution(price):
    if price >= 500000:
        return price * 8 // 10
    elif price >= 300000:
        return price * 9 // 10
    elif price >= 100000:
        return price * 95 // 100
    else:
        return price
    
    # 각 항목을 곱셈 후 나눗셈이 아닌 return price * 0.8 등으로도 표현 가능