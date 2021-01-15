class Solution {
    public int getMaximumGenerated(int n) {
        int[] arr = new int[n+1];
        arr[0] = 0;
        if(n==0)
            return arr[0];
        int max = 1;
        arr[1] = 1;
        for(int i=2;i<n+1;i++){
            if(i%2==0)
                arr[i] = arr[i/2];
            else
                arr[i] = arr[(i-1)/2] + arr[(i+1)/2];
            if(arr[i] > max)
                max = arr[i];
        }
        return max;
    }
}
