import java.util.Comparator;
import java.util.PriorityQueue;

class Solution {
    public int solution(int N, int[][] road, int K) {
        int answer = 0;

        int[][] maps = new int[N][N];
        for(int i=0; i<N; i++){
        	for(int j=0; j<N; j++){
        		maps[i][j] = Integer.MAX_VALUE;
        	}
        }
        // 최단 거리를 찾아야하므로 모든 값을 최대값으로 초기화

        for (int i=0; i<road.length; i++) {
            int x = road[i][0]-1;
            int y = road[i][1]-1;
            int w = road[i][2];
            if (w < maps[x][y]) {
            	maps[x][y] = maps[y][x] = w;
            } // maps에 최대값이 들어가 있으면 입력된 가중치가 들어감
        }

        boolean[] visited = new boolean[N]; // 방문 여부
        int[] d = new int[N]; // 최단거리
        for(int i=0; i<N; i++) {
        	d[i] = Integer.MAX_VALUE;
        }
        
        PriorityQueue<Integer> pq = new PriorityQueue<>(new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return Integer.compare(d[o1], d[o2]);
            } // 우선순위 큐는 비교연산자 Comparator로 정의해서 최단거리 비교해야 함
        });

        d[0] = 0;
        pq.add(0);
        // 0번째 index 노드 (출발노드)

        while(!pq.isEmpty()) {
            int cur = pq.poll();
            // pq에 존재하는 첫번 째 값 반환하고 그 값을 제거
            if (visited[cur]) continue;
            // 이미 방문했으면 건너뛰기

            visited[cur] = true;
            for (int i=0; i<N; i++) {
                if (maps[cur][i] == Integer.MAX_VALUE) continue;
                // 입력된 가중치가 없으면 넘어감

                if (d[i] > d[cur] + maps[cur][i]) {
                    d[i] = d[cur] + maps[cur][i];
                    pq.add(i);
                }
                // 최단 거리가 갱신되면 그 index를 pq에 추가해줘서 다른 최단거리도 변할 수 있도록 함
            }
        }

        for(int i=0; i<d.length; i++)
	    {
	    	if(d[i] <= K)
	    		answer++;
	    }

        return answer;
    }
}