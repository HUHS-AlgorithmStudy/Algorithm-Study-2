function solution(n) {
  let binary = '';
  while (n !== 0) {
    const remain = n % 3;
    binary = f(remain).toString() + binary;

    n = Math.ceil(n / 3) - 1;
  }
  return binary;
}

function f(n) {
  return n === 0 ? 4 : n;
}
