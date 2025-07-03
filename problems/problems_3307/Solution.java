package problems.problems_3307;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public char kthCharacter(long k, int[] operations) {
        int count = 0;
        while (k > 1) {
            int idx = 63 - Long.numberOfLeadingZeros(k - 1);
            if (operations[idx] == 1) {
                count++;
            }
            k -= 1L << idx;
        }
        return (char) ('a' + count % 26);
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        long k = Long.parseLong(inputJsonValues[0]);
		int[] operations = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(kthCharacter(k, operations));
    }
}
