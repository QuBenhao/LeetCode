package problems.problems_1689;

public class Solution {
    public int minPartitions(String n) {
        char[] chars = n.toCharArray();
        int max = 0;
        for (char aChar : chars) {
            if (aChar - '0' > max) {
                if (aChar == '9')
                    return 9;
                max = aChar - '0';
            }
        }
        return max;
    }
}