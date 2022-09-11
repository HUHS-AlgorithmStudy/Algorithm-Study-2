def solution(priorities, location):
    # 출력된 문서를 저장하는 변수
    printed = 0

    # 대기 목록에 문서가 있을 경우
    while len(priorities) > 0:
        first = priorities[0]
        # 첫 번째 문서가 가장 중요도가 높은 문서가 아닐 때
        if first < max(priorities):
            # 대기 목록에서 첫 번째 문서를 제거하고, 맨 뒤에 해당 문서를 넣는다.
            priorities.pop(0)
            priorities.append(first)
            # 맨 뒤로 넣은 문서가 '내가 인쇄를 요청한 문서'였다면 location의 값을 맨 뒤로 바꿔주기
            if location == 0:
                location = len(priorities) - 1
            # 그렇지 않다면 해당 문서의 인덱스를 한 칸 앞으로 빼주기
            else:
                location -= 1
        # 첫 번째 문서가 가장 중요도가 높은 문서일 때
        else:
            # 첫 번째 문서가 '내가 인쇄를 요청한 문서'일 때
            if location == 0:
                # 이미 출력된 문서들의 수에 1을 더해 return
                return printed + 1
            # 다른 문서가 가장 중요도가 높은 문서였을 때
            # 해당 문서를 제거하고 출력된 문서의 수를 하나 늘린 뒤, location의 값을 하나 빼준다.
            priorities.pop(0)
            printed += 1
            location -= 1
    return printed
