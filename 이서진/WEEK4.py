def solution(n, left, right):
    array = []
    for index in range(left, right+1):  # 한 행씩
        row = index // n  # /로 하면 float로 출력되어 int()해줘야 하는 이슈 발생해서 //로 변경
        column = index % n  # 나머지
        if row > column:
            array.append(row+1)
        else:
            array.append(column+1)

    return array
