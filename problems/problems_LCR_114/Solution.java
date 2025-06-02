package problems.problems_LCR_114;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String alienOrder(String[] words) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String[] words = jsonArrayToStringArray(inputJsonValues[0]);
        return JSON.toJSON(alienOrder(words));
    }
}
