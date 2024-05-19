package problems.problems_1688;


public class Solution {
    public int numberOfMatches(int n) {
        if (n == 1)
            return 0;
        int count = 0;
        while (n >= 2) {
            if (n % 2 == 0) {
                n /= 2;
                count += n;
            } else {
                count += (n - 1) / 2;
                n = (n + 1) / 2;
            }
        }
        return count;
    }
}