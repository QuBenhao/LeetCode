class Solution {
    public int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);
        int left = 0, right = people.length - 1, ans = 0;
        while(left < right){
            if(people[left] + people[right] <= limit)
                left++;
            right--;
            ans++;
        }
        if(left==right)
            ans++;
        return ans;
    }
}
