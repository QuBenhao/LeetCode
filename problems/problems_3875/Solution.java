package problems.problems_3875;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean uniformArray(int[] nums1) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums1 = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(uniformArray(nums1));
    }
}
