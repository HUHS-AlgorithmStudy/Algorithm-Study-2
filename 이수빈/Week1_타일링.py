def func(e):
    prev = 1
    pprev = 1
    v = 2

    while v <= e:
        a = (prev + pprev) % 1000000007
        pprev = prev
        prev = a
        v += 1
    return prev


def solution(n):
    answer = func(n)
    return answer
