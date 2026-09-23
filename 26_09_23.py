#Sum of divisors
def solution(n):
    w=0
    for x in range(1,n+1):
        if n%x==0:
            w=w+x
    answer = w
    return answer


#Finding numbers with a remainder of 1
def solution(n):
    m=n-1
    for x in range(1,m):
        if n%x==1:
            return x
    return m

