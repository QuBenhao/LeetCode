package problems.problems_2103;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int countPoints(String rings) {
        int[] count = new int[10];
        for (int i = 0; i < rings.length(); i += 2) {
            count[rings.charAt(i + 1) - '0'] |= 1 << ("RGB".indexOf(rings.charAt(i)));
        }
        int result = 0;
        for (int i = 0; i < count.length; i++) {
            if (count[i] == (1 << 3) - 1) { // Check if all three colors are present
                result++;
            }
        }
        return result;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String rings = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(countPoints(rings));
    }
}
