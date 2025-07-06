package problems.problems_3602;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private static final String HEX36 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    public String concatHex36(int n) {
        int x = n * n;
        int y = x * n;
        StringBuilder sb = new StringBuilder();
        while (y > 0) {
            sb.append(HEX36.charAt(y % 36));
            y /= 36;
        }
        while (x > 0) {
            sb.append(HEX36.charAt(x % 16));
            x /= 16;
        }
        sb.reverse();
        return sb.toString();
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
        return JSON.toJSON(concatHex36(n));
    }
}
