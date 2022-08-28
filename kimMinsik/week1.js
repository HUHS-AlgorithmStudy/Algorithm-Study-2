//최종풀이
function solution(n) {
  let tmp = [1, 2];
  for (let i = 2; i < n; i++) {
    tmp.push((tmp[i - 1] + tmp[i - 2]) % 1000000007);
  }

  return tmp[n - 1];
}
