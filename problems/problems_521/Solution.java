package problems.problems_521;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int findLUSlength(String a, String b) {

    }

    @Override
    public Object solve(String[] values) {
        String a = jsonStringToString(values[0]);
		String b = jsonStringToString(values[1]);
        return JSON.toJSON(findLUSlength(a, b));
    }
}
