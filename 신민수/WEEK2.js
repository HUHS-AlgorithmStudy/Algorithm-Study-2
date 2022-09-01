function solution(priorities, location) {
  let index = 0;

  while (true) {
    const max = Math.max(...priorities);
    const current = priorities.shift();

    if (current !== max) {
      priorities.push(current);
      location = (location === 0 ? priorities.length : location) - 1;
      continue;
    }

    index++;

    if (location === 0) {
      return index;
    }

    location--;
  }
}
