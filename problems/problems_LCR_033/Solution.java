package problems.problems_LCR_033;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<List<String>> groupAnagrams(String[] strs) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String[] strs = jsonArrayToStringArray(inputJsonValues[0]);
        return JSON.toJSON(groupAnagrams(strs));
    }
}
