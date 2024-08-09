package problems.problems_139;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean wordBreak(String s, List<String> wordDict) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
		List<String> wordDict = jsonArrayToStringList(inputJsonValues[1]);
        return JSON.toJSON(wordBreak(s, wordDict));
    }
}
