package sep1;

public class n87390 {

	public static void main(String[] args) {
		class Solution {
			
			 public int[] solution(int n, long left, long right) {
				  	int[] answer = new int[(int) (right - left + 1)];
				  	int index = 0;
			        for(long i=left; i <= right; i++)
			        {
			        	int a = (int) i / n;
			        	int b = (int) i % n;
			        	if(a > b)
			        		answer[index] = a + 1;
			        	else
			        		answer[index] = b + 1;
			        	index++;
			        }
			        return answer;
			    }
		}
			
		
		Solution sol = new Solution();
		int[] test = sol.solution(3,2,5);
		for(int i : test) {
			System.out.println(i);
		}

	}

}
