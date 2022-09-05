function solution(number, k) {
  let answer = "";
  let array = number.split("").map((item) => parseInt(item));
  let length = number.length - k;
  let index = 0;
  let cnt = 1;

  for (let i = 0; i < length; i++) {
    let max = 0;
    for (let j = index; j < number.length - length + cnt; j++) {
      if (max < array[j]) {
        max = array[j];
        index = j;
      }
    }
    answer += max;
    array[index] = 0;
    cnt++;
  }
  return answer;
}
