package problems.problems_763;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<Integer> partitionLabels(String s) {

    }

    @Override
    public Object solve(String[] values) {
        String s = jsonStringToString(values[0]);
        return JSON.toJSON(partitionLabels(s));
    }
}
