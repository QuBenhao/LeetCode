package problems.problems_3304;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public char kthCharacter(int k) {
        int count = 0;
        while (k > 1) {
            k -= 1 << (31 - Integer.numberOfLeadingZeros(k - 1));
            count++;
        }
        return (char) ('a' + count % 26);
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int k = Integer.parseInt(inputJsonValues[0]);
        return JSON.toJSON(kthCharacter(k));
    }
}
