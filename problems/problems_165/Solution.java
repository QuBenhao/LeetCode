package problems.problems_165;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int compareVersion(String version1, String version2) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String version1 = jsonStringToString(inputJsonValues[0]);
		String version2 = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(compareVersion(version1, version2));
    }
}
