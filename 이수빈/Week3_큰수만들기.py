def solution(number, k):
    left = 0
    right = 1
    result_len = len(number) - k  # return할 숫자의 자릿수
    while len(number) >= result_len and right < len(number):
        if len(number) == result_len:
            return number
        if number[left] < number[right]:  # 왼쪽 숫자가 오른쪽 숫자보다 작으면 왼쪽 숫자 삭제
            number = number.replace(number[left], '', 1)
            if left > 0:  # 왼쪽 숫자가 number의 첫 번째 숫자가 아닌 경우 처음부터 다시 비교하도록 인덱스 조정
                left -= 1
                right -= 1
        else:  # 오른쪽 숫자가 크거나 왼쪽과 오른쪽 숫자가 같을 경우 그 다음 숫자들을 비교하기 위해 인덱스 조정
            left += 1
            right += 1
    if len(number) > result_len:  # 만약 11111 등 각 숫자의 크기 차이가 없는 숫자가 올 경우 슬라이싱으로 숫자 길이 조정
        number = number[:result_len]
    return number
