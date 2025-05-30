package problems.problems_LCR_071;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import com.alibaba.fastjson.JSON;

import qubhjava.BaseSolution;


class S {
	private final int[] prefix;
	private final Random random;
    public S(int[] w) {
		int n = w.length;
		prefix = new int[n+1];
		for (int i = 0; i < n; i++) {
			prefix[i+1] = prefix[i] + w[i];
		}
		random = new Random();
    }
    
    public int pickIndex() {
		int n = prefix.length-1;
		int v = random.nextInt(prefix[n]) + 1;
		int left = 0, right = n;
		while (left < right) {
			int mid = ((right - left) >> 1) + left;
			if (prefix[mid] < v) {
				left = mid + 1;
			} else {
				right = mid;
			}
		}
		return left - 1;
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
		S obj = new S(w);
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
