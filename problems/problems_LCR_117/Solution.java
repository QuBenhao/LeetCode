package problems.problems_LCR_117;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int numSimilarGroups(String[] strs) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String[] strs = jsonArrayToStringArray(inputJsonValues[0]);
        return JSON.toJSON(numSimilarGroups(strs));
    }
}
