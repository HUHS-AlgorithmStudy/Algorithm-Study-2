function solution(number, k) {
  let max = 0;
  let maxMax = "";
  let length = number.length - k;

  for (let i = 0; i < length; i++) {
    for (let j = 0; j < number.length; j++) {
      max = parseInt(number[j]);
      if (parseint(number[j]) < parseint(number[j + 1])) {
        max = parseint(number[j + 1]);
      }
    }
    maxMan += max;
    number.number.indexOf(max);
  }

  return answer;
}

//number를 배열로 만들기는 해야될듯.
