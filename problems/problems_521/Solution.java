package problems.problems_521;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int findLUSlength(String a, String b) {
        return a.compareTo(b) == 0 ? -1 : Math.max(a.length(), b.length());
    }

    @Override
    public Object solve(String[] values) {
        String a = jsonStringToString(values[0]);
		String b = jsonStringToString(values[1]);
        return JSON.toJSON(findLUSlength(a, b));
    }
}
