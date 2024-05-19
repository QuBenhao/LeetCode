package problems.problems_1662;

public class Solution {
    public boolean arrayStringsAreEqual(String[] word1, String[] word2) {
        int i1 = 0, w1 = 0, i2 = 0, w2 = 0;
        while (i1 < word1.length && i2 < word2.length) {
            if (word1[i1].charAt(w1) != word2[i2].charAt(w2))
                return false;
            w1++;
            w2++;
            if (w1 == word1[i1].length()) {
                w1 = 0;
                i1++;
            }
            if (w2 == word2[i2].length()) {
                w2 = 0;
                i2++;
            }
        }
        return i1 == word1.length && i2 == word2.length;
    }
}
