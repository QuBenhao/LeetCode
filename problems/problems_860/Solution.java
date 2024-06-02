package problems.problems_860;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean lemonadeChange(int[] bills) {

    }

    @Override
    public Object solve(String[] values) {
        int[] bills = jsonArrayToIntArray(values[0]);
        return JSON.toJSON(lemonadeChange(bills));
    }
}
