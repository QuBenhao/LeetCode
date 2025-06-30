package problems.problems_3330;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int possibleStringCount(String word) {
        int ans = 1;
        for (int i = 0; i < word.length() - 1; i++) {
            if (word.charAt(i) == word.charAt(i + 1)) {
                ans++;
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String word = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(possibleStringCount(word));
    }
}
