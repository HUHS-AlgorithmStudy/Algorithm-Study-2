package sep1;

public class n12899 {
	
	class Solution {
	    public String solution(int n) {
	    	
	    	
	    	String[] num = {"4","1","2"}; // 0 1 2
	        String answer = "";
	    	
	    	while(n > 0)
	    	{
	    		int tmp = n % 3;
	    		answer = num[tmp] + answer;
	    		n /= 3;
	    		if(tmp == 0)
	    			n--;
	    	}

	        return answer;
	    }
	}
}
