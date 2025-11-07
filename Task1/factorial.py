# 팩토리얼 함수
def factorial(n):
    if n < 0:
        raise ValueError("음수의 팩토리얼은 정의되지 않습니다.")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# 소수판별 함수
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True