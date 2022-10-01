def solution(n):
    answer = ''
    number = 0  # 124나라의 숫자

    while n > 0:
        if n % 3 == 0:
            number = 4  # n을 3으로 나눈 나머지가 0일 경우 124나라에서는 4로 바꿔주기
            # 이는 3의 배수인 경우이기 때문에 다음에 확인할 수를 n // 3 - 1로 바꾸어 주기(e.g. 3의 경우 n//3이 0이 아닌 1이 되기 때문)
            n = n // 3 - 1
        else:
            number = n % 3  # 그렇지 않은 경우 해당 숫자를 그대로 할당하기
            n //= 3
        answer = str(number) + answer  # answer 앞에 숫자 붙여 주기

    return answer
