package problems.problems_LCR_002;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String addBinary(String a, String b) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String a = jsonStringToString(inputJsonValues[0]);
		String b = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(addBinary(a, b));
    }
}
