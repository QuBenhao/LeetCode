package problems.problems_3474;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String generateString(String str1, String str2) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String str1 = jsonStringToString(inputJsonValues[0]);
		String str2 = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(generateString(str1, str2));
    }
}
