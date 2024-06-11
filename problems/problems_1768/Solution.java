package problems.problems_1768;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder sb = new StringBuilder();
        int m = Math.min(word1.length(), word2.length());
        for (int i = 0; i < m; i++) {
            sb.append(word1.charAt(i));
            sb.append(word2.charAt(i));
        }
        sb.append(word1.substring(m));
        sb.append(word2.substring(m));
        return sb.toString();
    }



    @Override
    public Object solve(String[] values) {
        String word1 = values[0];
		String word2 = values[1];
        return JSON.toJSON(mergeAlternately(word1, word2));
    }
}
