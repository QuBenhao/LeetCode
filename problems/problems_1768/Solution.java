package problems.problems_1768;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String mergeAlternately(String word1, String word2) {

    }

    @Override
    public Object solve(String[] values) {
        String word1 = values[0];
		String word2 = values[1];
        return JSON.toJSON(mergeAlternately(word1, word2));
    }
}
