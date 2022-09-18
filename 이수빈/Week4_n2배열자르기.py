def solution(n, left, right):
    answer = []

    # 효율을 위해 left와 right가 위치한 구간을 포함한 곳만 append한다
    for i in range(left // n, right // n + 1):
        for j in range(i):
            answer.append(i + 1)

        for j in range(i + 1, n + 1):
            answer.append(j)

    return answer[left % n:len(answer) - (n - 1) + right % n]

# 1 2 3 4 5
# 2 2 3 4 5
# 3 3 3 4 5
# 4 4 4 4 5
# 5 5 5 5 5

# => 1 2 3 4 5   2 2 3 4 5   3 3 3 4 5   4 4 4 4 5   5 5 5 5 5

# right 자르는 개수 right % n
# 19    0          4
# 18    1          3
# 17    2          2
# 16    3          1
# 15    4          0
# 14    0          4

# => (n - 1) - right % n
