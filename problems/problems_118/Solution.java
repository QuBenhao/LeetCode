package problems.problems_118;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> ans = new ArrayList<>(numRows);
        for (int i = 0; i < numRows; i++) {
            List<Integer> row = new ArrayList<>(i + 1), lastRow = i > 0 ? ans.get(i - 1) : null;
            row.add(1);
            for (int j = 1; j < i; j++) {
                row.add(lastRow.get(j - 1) + lastRow.get(j));
            }
            if (i > 0) {
                row.add(1);
            }
            ans.add(row);
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int numRows = Integer.parseInt(inputJsonValues[0]);
        return JSON.toJSON(generate(numRows));
    }
}
