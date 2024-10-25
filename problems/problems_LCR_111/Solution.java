package problems.problems_LCR_111;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        List<List<String>> equations = jsonArrayToString2DList(inputJsonValues[0]);
		double[] values = FIXME(inputJsonValues[1])
		List<List<String>> queries = jsonArrayToString2DList(inputJsonValues[2]);
        return JSON.toJSON(calcEquation(equations, values, queries));
    }
}
