def solution(number, k):
    answer_array = []  # 정답 숫자들이 담길 배열
    _k = len(number) - k  # 구해야 하는 숫자의 길이
    turn = 0  # number 배열의 몇 번째 위치를 보고 있는지 알려주는 변수

    for n in number:  # number 하나씩 돌려가면서
        # 지금 보는 숫자가 마지막 숫자보다 더 크고, 배열에 남은 개수가 더 추가해야 하는 개수보다 크거나 비슷하다면
        while (n > answer_array[-1] if answer_array else False) and len(number[turn:]) > (_k - len(answer_array)):
            answer_array.pop()  # 마지막 숫자 뺌 (교체를 위해)

        if len(answer_array) < _k:  # 구해야 하는 숫자 길이를 채우지 못했다면 (교체되는 숫자일 경우에도 위에서 이미 pop 했으므로 해당 조건 만족함)
            answer_array.append(n)  # 맨 뒤에 집어넣음

        # 정답 숫자수만큼의 길이가 채워져 있다면 아무것도 X
        turn += 1  # 이제 넘어가니까 turn + 1

    return ''.join(answer_array)