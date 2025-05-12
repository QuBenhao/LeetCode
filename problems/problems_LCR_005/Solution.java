package problems.problems_LCR_005;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxProduct(String[] words) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String[] words = jsonArrayToStringArray(inputJsonValues[0]);
        return JSON.toJSON(maxProduct(words));
    }
}
