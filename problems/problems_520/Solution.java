package problems.problems_520;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean detectCapitalUse(String word) {

    }

    @Override
    public Object solve(String[] values) {
        String word = jsonStringToString(values[0]);
        return JSON.toJSON(detectCapitalUse(word));
    }
}
