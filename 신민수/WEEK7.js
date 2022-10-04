function solution(dirs) {
  let count = 0;
  let position = [0, 0];
  const visited = new Map();
  for (let i=0; i<dirs.length; i++) {
    const input = dirs[i];
    const moveTo = move(input, position);
    if (Math.abs(moveTo[0]) > 5 || Math.abs(moveTo[1]) > 5) {
      continue;
    }

    const a = position < moveTo ? position.join() : moveTo.join();
    const b = position < moveTo ? moveTo.join() : position.join();

    if (!(visited.has(a) && visited.get(a).includes(b))) {
      visited.set(a, [...(visited.get(a) || []), b]);
      count++;
    }
    position = moveTo;
  }
  return count;
}

function move(input, position) {
  switch (input) {
    case 'U':
      return [position[0], position[1] + 1];
    case 'D':
      return [position[0], position[1] - 1];
    case 'L':
      return [position[0] + 1, position[1]];
    case 'R':
      return [position[0] - 1, position[1]];
  }

  return position;
}
