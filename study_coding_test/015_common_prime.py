def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def removeCommonPrimeDivisors(x, g):
    # g의 소인수로 x를 나눠가며 x를 줄임
    while x != 1:
        x_gcd = gcd(x, g)
        if x_gcd == 1:
            break
        x //= x_gcd
    return x

def hasSamePrimeDivisors(a, b):
    g = gcd(a, b)
    a_rem = removeCommonPrimeDivisors(a, g)
    if a_rem != 1:
        return False
    b_rem = removeCommonPrimeDivisors(b, g)
    if b_rem != 1:
        return False
    return True

def solution(A, B):
    count = 0
    for a, b in zip(A, B):
        if hasSamePrimeDivisors(a, b):
            count += 1
    return count


A = [15, 10, 3]
B = [75, 30, 5]
print(solution(A, B))