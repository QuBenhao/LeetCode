package problems.problems_3370;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int smallestNumber(int n) {
        int bitLength = 32 - Integer.numberOfLeadingZeros(n);
        return (1 << bitLength) - 1;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
        return JSON.toJSON(smallestNumber(n));
    }
}
