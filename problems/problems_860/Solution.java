package problems.problems_860;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean lemonadeChange(int[] bills) {
        int fives = 0, tens = 0;
        for (int bill: bills) {
            if (bill == 5) {
                fives++;
            } else if (bill == 10) {
                tens++;
                fives--;
            } else if (tens > 0) {
                tens--;
                fives--;
            } else {
                fives -= 3;
            }
            if (fives < 0) {
                return false;
            }
        }
        return true;
    }

    @Override
    public Object solve(String[] values) {
        int[] bills = jsonArrayToIntArray(values[0]);
        return JSON.toJSON(lemonadeChange(bills));
    }
}
