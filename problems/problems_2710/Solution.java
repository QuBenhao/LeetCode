package problems.problems_2710;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String removeTrailingZeros(String num) {

    }

    @Override
    public Object solve(String[] values) {
        String num = jsonStringToString(values[0]);
        return JSON.toJSON(removeTrailingZeros(num));
    }
}
