package problems.problems_LCR_065;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minimumLengthEncoding(String[] words) {
        int n = words.length;
        String[] reversedWords = new String[n];
        for (int i = 0; i < n; i++) {
            reversedWords[i] = new StringBuilder(words[i]).reverse().toString();
        }
        Arrays.sort(reversedWords);
        int res = 0;
        for (int i = 0; i < n; i++) {
            if (i + 1 < n && reversedWords[i + 1].startsWith(reversedWords[i])) {
                continue;
            }
            res += reversedWords[i].length() + 1;
        }
        return res;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String[] words = jsonArrayToStringArray(inputJsonValues[0]);
        return JSON.toJSON(minimumLengthEncoding(words));
    }
}
