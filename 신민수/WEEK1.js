function solution(n) {
  if (n <= 3) return n

  const sequence = [1, 2, 3]
  for (let i = 4; i <= n; i++) {
    sequence.push((sequence[sequence.length - 2] + sequence[sequence.length - 1]) % 1000000007)
  }
  return sequence.pop()
}
