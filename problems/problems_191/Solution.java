package problems.problems_191;

public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int count = 0;
        for (; n != 0; n = n & (n - 1))
            count++;
        return count;
    }
}
