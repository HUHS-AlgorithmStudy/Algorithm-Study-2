// 최종풀이
function solution(priorities, location) {
  let index = priorities.map((x, i) => [x, i]);
  let cnt = 0;

  while (true) {
    let tmp = index.shift();
    let max = Math.max(...index.map((x) => x[0]));
    if (tmp[0] >= max) {
      cnt++;
      if (location === tmp[1]) {
        return cnt;
      }
    } else {
      index.push(tmp);
    }
  }
}
