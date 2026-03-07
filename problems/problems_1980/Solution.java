package problems.problems_1980;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String findDifferentBinaryString(String[] nums) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String[] nums = jsonArrayToStringArray(inputJsonValues[0]);
        return JSON.toJSON(findDifferentBinaryString(nums));
    }
}
