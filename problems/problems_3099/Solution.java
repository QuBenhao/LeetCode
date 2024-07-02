package problems.problems_3099;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int sumOfTheDigitsOfHarshadNumber(int x) {
        int s = 0;
        for (int num = x; num > 0; num /= 10) {
            s += num % 10;
        }
        return x % s == 0 ? s : -1;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int x = Integer.parseInt(inputJsonValues[0]);
        return JSON.toJSON(sumOfTheDigitsOfHarshadNumber(x));
    }
}
