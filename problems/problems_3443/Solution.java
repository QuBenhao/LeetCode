package problems.problems_3443;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxDistance(String s, int k) {
        int n = s.length();
        int ans = 0;
        int x = 0, y = 0;
        k *= 2;
        for (int i = 0; i < n; ++i) {
            switch (s.charAt(i)) {
                case 'N':
                    ++y;
                    break;
                case 'S':
                    --y;
                    break;
                case 'E':
                    ++x;
                    break;
                case 'W':
                    --x;
                    break;
            }
            ans = Math.max(ans, Math.min(i + 1, k + Math.abs(x) + Math.abs(y)));
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(maxDistance(s, k));
    }
}
