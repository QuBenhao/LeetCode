package problems.problems_LCR_071;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


class Solution {

    public Solution(int[] w) {

    }
    
    public int pickIndex() {

    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(w);
 * int param_1 = obj.pickIndex();
 */

public class Solution extends BaseSolution {


    @Override
    public Object solve(String[] inputJsonValues) {
        String[] operators = jsonArrayToStringArray(inputJsonValues[0]);
		String[][] opValues = jsonArrayToString2DArray(inputJsonValues[1]);
		int[] w = jsonArrayToIntArray(opValues[0][0]);
		Solution obj = new Solution(w);
		List<Object> ans = new ArrayList<>(operators.length);
		ans.add(null);
		for (int i = 1; i < operators.length; i++) {
			if (operators[i].compareTo("pickIndex") == 0) {
				
				ans.add(obj.pickIndex());
				continue;
			}
			ans.add(null);
		}
        return JSON.toJSON(ans);
    }
}
