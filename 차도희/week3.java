package sep1;

import java.util.Arrays;


public class n42883 {

	public static void main(String[] args) {
		
		class Solution {
		    public String solution(String number, int k) {
		    	
		    	char[] arr = number.toCharArray();
		    	int[] answer = new int[arr.length - k];
		    	int start = 0, end = k, temp, index;
		    	int i = 0; // answer의 index
		    
		    	while(end < arr.length)
		    	{
		    		temp = 0;
		    		index = start;
		    		while(start<=end)
		    		{
		    			if(arr[start]-'0' > temp)
		    			{
		    				temp = arr[start] - '0';
		    				index = start;
                            // start ~ end 범위에서 가장 큰 수를 찾음
		    				// 포함하기로 한 숫자의 왼편은 필요 없으므로 그 수의 index도 함께 저장
		    			}
		    			start++;
		    		}
		    		answer[i] = temp;
		    		start = index + 1; 
		    		end++;
		    		i++;
		    	}
		    	
		    	String strArray = Arrays.toString(answer).replaceAll("\\[|]|,| ", "");
		    	//int 배열을 문자열로 정리
		        return strArray;
		    }
		}
		
		Solution sol = new Solution();
		System.out.println(sol.solution("42974102378", 5)); 

	}

}
