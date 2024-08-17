package problems.problems_LCR_059;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


class KthLargest {

    public KthLargest(int k, int[] nums) {

    }
    
    public int add(int val) {

    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */

public class Solution extends BaseSolution {


    @Override
    public Object solve(String[] inputJsonValues) {
        String[] operators = jsonArrayToStringArray(inputJsonValues[0]);
		String[][] opValues = jsonArrayToString2DArray(inputJsonValues[1]);
		int k = Integer.parseInt(opValues[0][0]);
		int[] nums = jsonArrayToIntArray(opValues[0][1]);
		KthLargest obj = new KthLargest(k, nums);
		List<Object> ans = new ArrayList<>(operators.length);
		ans.add(null);
		for (int i = 1; i < operators.length; i++) {
			if (operators[i].compareTo("add") == 0) {
				int val = Integer.parseInt(opValues[i][0]);
				ans.add(obj.add(val));
				continue;
			}
			ans.add(null);
		}
        return JSON.toJSON(ans);
    }
}
