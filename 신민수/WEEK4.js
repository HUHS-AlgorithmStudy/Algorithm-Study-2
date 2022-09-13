function solution(n, left, right) {
  const a = [];
  for (let i=left; i<=right; i++) {
    const x = i % n;
    const y = Math.floor(i / n);
    a.push(Math.max(x, y) + 1);
  }
  return a;
}
