package problems.problems_2566;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minMaxDifference(int num) {
        String s = Integer.toString(num);
        int mx = num;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) != '9') {
                String tmp = s.replace(s.charAt(i), '9');
                mx = Integer.parseInt(tmp);
                break;
            }
        }
        String tmp = s.replace(s.charAt(0), '0');
        return mx - Integer.parseInt(tmp);
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int num = Integer.parseInt(inputJsonValues[0]);
        return JSON.toJSON(minMaxDifference(num));
    }
}
