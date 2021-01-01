class Solution {
    public boolean canFormArray(int[] arr, int[][] pieces) {
        StringBuilder str = new StringBuilder();
        for(int n:arr){
            str.append(n);
            str.append("#");
        }
        for(int i=0;i<pieces.length;i++){
            StringBuilder substr = new StringBuilder();
            for(int n:pieces[i]){
                substr.append(n);
                substr.append("#");
            }
            if(!str.toString().contains(substr.toString()))
                return false;
        }
        return true;
    }
}
