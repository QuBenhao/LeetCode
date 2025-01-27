package problems.problems_119;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<Integer> getRow(int rowIndex) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int rowIndex = Integer.parseInt(inputJsonValues[0]);
        return JSON.toJSON(getRow(rowIndex));
    }
}
