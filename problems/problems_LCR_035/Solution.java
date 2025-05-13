package problems.problems_LCR_035;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int findMinDifference(List<String> timePoints) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        List<String> timePoints = jsonArrayToStringList(inputJsonValues[0]);
        return JSON.toJSON(findMinDifference(timePoints));
    }
}
