def isExistHigherPriority(priorities):
    for p in priorities[1:]:
        if priorities[0] < p:
            return True

    return False


def solution(priorities, location):
    answer = location + 1
    totalNum = len(priorities)

    while len(priorities):  # 다 출력되기 전까지
        if isExistHigherPriority(priorities):  # 검사하는 타겟이 우선순위가 가장 높은 게 아니라면
            priorities.append(priorities[0])  # 맨 뒤로 넣기

            if location == 0:  # 맨 뒤로 보내지는 게 location이라면
                location = len(priorities) - 2  # location 맨 뒤로 변경 (아직 맨 뒤로 넣은 거 삭제 안 된 것 반영)
                answer = totalNum  # 출력 순서 맨 뒤로 변경

            else:  # 맨 앞이 location이 아니라면
                location -= 1  # 위치 앞당겨짐
                answer -= 1  # 출력 순서 앞당겨짐

            del priorities[0]  # 삭제

        else:  # 출력
            if location == 0:  # location의 우선순위가 가장 높다면
                return answer  # 바로 출력이니 정답 리턴

            del priorities[0]  # 그게 아니라면 다시 삭제
            location -= 1  # location 변경
