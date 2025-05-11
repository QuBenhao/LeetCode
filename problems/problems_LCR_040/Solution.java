package problems.problems_LCR_040;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maximalRectangle(String[] matrix) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String[] matrix = jsonArrayToStringArray(inputJsonValues[0]);
        return JSON.toJSON(maximalRectangle(matrix));
    }
}
