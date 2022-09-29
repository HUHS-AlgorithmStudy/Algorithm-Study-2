function solution(N, road, K) {
  const town = new Map();

  const dfs = (position, time, visited) => {
    if (time > K) return;
    if (town.has(position) && town.get(position) <= time) return;

    town.set(position, time);
    if (town.size === N) return;

    const v = new Set(visited);
    v.add(position);
    if (v.size === N) return;

    for (let i=0; i<road.length; i++) {
      const [pos1, pos2, t] = road[i];
      if (position === pos1 && !v.has(pos2)) {
        dfs(pos2, time + t, v);
      }
      if (position === pos2 && !v.has(pos1)) {
        dfs(pos1, time + t, v);
      }
    }
  }

  dfs(1, 0, new Set());
  
  return town.size;
}
