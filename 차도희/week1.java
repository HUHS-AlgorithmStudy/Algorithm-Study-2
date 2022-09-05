class Solution {
    public int solution(int n) {
        int[] arr = new int[n+1];
        arr[0] = 1;
        arr[1] = 2;
        int index = 2;
        while(index < n)
        {
            arr[index] = (arr[index-1] + arr[index-2]) % 1000000007;
            index++;
        }
        
        return (arr[n-1]);
    }
}