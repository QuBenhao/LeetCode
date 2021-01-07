class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character,Integer> map = new HashMap<>();
        int j = 0,ans = 0;
        for(int i = 0; i < s.length(); i++){
            if(map.containsKey(s.charAt(i))){
                j = Math.max(j,map.get(s.charAt(i)));
            }
            ans = Math.max(ans,i-j+1);
            map.put(s.charAt(i),i+1);
        }
        return ans;
    }
}
