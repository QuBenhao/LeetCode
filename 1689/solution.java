class Solution {
    public int minPartitions(String n) {
        char[] chars = n. toCharArray();
        int max = 0;
        for(int i=0;i<chars.length;i++){
            if(chars[i] - '0' > max){
                if(chars[i] == '9')
                    return 9;
                max = chars[i] - '0';
            }
        }
        return max;
    }
}