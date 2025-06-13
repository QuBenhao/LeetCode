package problems.problems_2125;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int numberOfBeams(String[] bank) {
        int ans = 0;
        int prev = 0;
        for (String row: bank) {
            int count = 0;
            for (int i = 0; i < row.length(); i++) {
                if (row.charAt(i) == '1') {
                    count++;
                }
            }
            if (count > 0) {
                ans += prev * count;
                prev = count;
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String[] bank = jsonArrayToStringArray(inputJsonValues[0]);
        return JSON.toJSON(numberOfBeams(bank));
    }
}
