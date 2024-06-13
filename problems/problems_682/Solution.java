package problems.problems_682;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int calPoints(String[] operations) {

    }

    @Override
    public Object solve(String[] values) {
        String[] operations = jsonArrayToStringArray(values[0]);
        return JSON.toJSON(calPoints(operations));
    }
}
