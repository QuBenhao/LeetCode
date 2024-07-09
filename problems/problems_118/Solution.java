package problems.problems_118;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<List<Integer>> generate(int numRows) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int numRows = Integer.parseInt(inputJsonValues[0]);
        return JSON.toJSON(generate(numRows));
    }
}
