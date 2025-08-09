package problems.problems_869;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private static final List<Map<Integer, Integer>> digitCountMap = new ArrayList<>(31);
    static {
        for (int i = 0; i < 31; i++) {
            int num = 1 << i;
            Map<Integer, Integer> digitCount = new HashMap<>();
            while (num > 0) {
                int digit = num % 10;
                digitCount.put(digit, digitCount.getOrDefault(digit, 0) + 1);
                num /= 10;
            }
            digitCountMap.add(digitCount);
        }
    }
    public boolean reorderedPowerOf2(int n) {
        Map<Integer, Integer> digitCount = new HashMap<>();
        while (n > 0) {
            int digit = n % 10;
            digitCount.put(digit, digitCount.getOrDefault(digit, 0) + 1);
            n /= 10;
        }
        for (Map<Integer, Integer> powerDigits : digitCountMap) {
            if (powerDigits.equals(digitCount)) {
                return true;
            }
        }
        return false;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
        return JSON.toJSON(reorderedPowerOf2(n));
    }
}
