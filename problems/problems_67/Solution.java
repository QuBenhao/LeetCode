package problems.problems_67;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String addBinary(String a, String b) {

    }

    @Override
    public Object solve(String[] values) {
        String a = jsonStringToString(values[0]);
		String b = jsonStringToString(values[1]);
        return JSON.toJSON(addBinary(a, b));
    }
}
