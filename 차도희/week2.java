
import java.util.LinkedList;
import java.util.Arrays;
public class n42587 {

	public static void main(String[] args) {
		
		class Solution {
		    public int solution(int[] priorities, int location) {
		        int answer = 0;
		        LinkedList<Integer> pri = new LinkedList<Integer>();
		        LinkedList<Integer> index = new LinkedList<Integer>();
                // 주어진 배열과 그 배열의 index를 담는 linkedlist

		        int len = priorities.length;
		        
		        for(int n=0; n<len; n++)
		        {
		            pri.add(priorities[n]);
		            index.add(n);
		        }
		        
		        Arrays.sort(priorities);
                // 우선순위 오름차순 정렬
		        LinkedList<Integer> ans = new LinkedList<Integer>();
		        int i = len-1;
		        
		        while(!pri.isEmpty())
		        {
		            if(pri.get(0) == priorities[i])
		            {
		                ans.add(index.get(0));
                        // 우선순위인 index를 다른 배열에 차례대로 저장해둠
		                i--;
                        // 다음 우선순위로 넘어감
		            }
		            else
		            {
		                int tmp = index.get(0);
		                index.add(tmp);
		                tmp = pri.get(0);
		                pri.add(tmp);
                        // 우선순위가 아니면 맨 뒤로 옮겨줌
		            }
		            index.remove(0);
		            pri.remove(0);
		        }
		        
		        answer = ans.indexOf(location) + 1;
		        return answer;
		    }
		}

        /* test
		Solution sol = new Solution();
		int[] arr = {1,1,9,1,1,1};
		System.out.println(sol.solution(arr, 0));
        */
		
	}
}
