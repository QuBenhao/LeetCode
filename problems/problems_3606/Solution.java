package problems.problems_3606;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<String> validateCoupons(String[] code, String[] businessLine, boolean[] isActive) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String[] code = jsonArrayToStringArray(inputJsonValues[0]);
		String[] businessLine = jsonArrayToStringArray(inputJsonValues[1]);
		boolean[] isActive = FIXME(inputJsonValues[2])
        return JSON.toJSON(validateCoupons(code, businessLine, isActive));
    }
}
