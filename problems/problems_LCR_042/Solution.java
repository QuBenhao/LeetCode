package problems.problems_LCR_042;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


class RecentCounter {

    public RecentCounter() {

    }
    
    public int ping(int t) {

    }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter obj = new RecentCounter();
 * int param_1 = obj.ping(t);
 */

public class Solution extends BaseSolution {


    @Override
    public Object solve(String[] inputJsonValues) {
        String[] operators = jsonArrayToStringArray(inputJsonValues[0]);
		String[][] opValues = jsonArrayToString2DArray(inputJsonValues[1]);
		
		RecentCounter obj = new RecentCounter();
		List<Object> ans = new ArrayList<>(operators.length);
		ans.add(null);
		for (int i = 1; i < operators.length; i++) {
			if (operators[i].compareTo("ping") == 0) {
				int t = Integer.parseInt(opValues[i][0]);
				ans.add(obj.ping(t));
				continue;
			}
			ans.add(null);
		}
        return JSON.toJSON(ans);
    }
}
