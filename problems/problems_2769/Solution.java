package problems.problems_2769;

import com.alibaba.fastjson.JSON;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int theMaximumAchievableX(int num, int t) {
        return num + 2 * t;
    }

    @Override
    public Object solve(String[] values) {
        int num = Integer.parseInt(values[0]);
		int t = Integer.parseInt(values[1]);
        return JSON.toJSON(theMaximumAchievableX(num, t));
    }
}
