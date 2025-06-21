package problems.problems_2138;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String[] divideString(String s, int k, char fill) {
        int n = s.length();
        String[] result = new String[(n + k - 1) / k];
        for (int i = 0; i < n; i += k) {
            if (i + k <= n) {
                result[i / k] = s.substring(i, i + k);
            } else {
                result[i / k] = s.substring(i) + String.valueOf(fill).repeat(i + k - n);
            }
        }
        return result;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
		char fill = inputJsonValues[2].length() > 1 ? inputJsonValues[2].charAt(1) : inputJsonValues[2].charAt(0);
        return JSON.toJSON(divideString(s, k, fill));
    }
}
