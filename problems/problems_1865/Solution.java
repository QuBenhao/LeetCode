package problems.problems_1865;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


class FindSumPairs {

	private final Map<Integer, Integer> nums1_map = new HashMap<>();
	private final Map<Integer, Integer> nums2_map = new HashMap<>();
	private final int[] nums2;

    public FindSumPairs(int[] nums1, int[] nums2) {
        this.nums2 = nums2;
        for (int num : nums1) {
            nums1_map.put(num, nums1_map.getOrDefault(num, 0) + 1);
        }
        for (int num : nums2) {
            nums2_map.put(num, nums2_map.getOrDefault(num, 0) + 1);
        }
    }
    
    public void add(int index, int val) {
        nums2_map.put(nums2[index], nums2_map.getOrDefault(nums2[index], 0) - 1);
        nums2[index] += val;
        nums2_map.put(nums2[index], nums2_map.getOrDefault(nums2[index], 0) + 1);
    }
    
    public int count(int tot) {
        int count = 0;
        for (Map.Entry<Integer, Integer> entry : nums1_map.entrySet()) {
            int num1 = entry.getKey();
            int freq1 = entry.getValue();
            count += nums2_map.getOrDefault(tot - num1, 0) * freq1;
        }
        return count;
    }
}

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * FindSumPairs obj = new FindSumPairs(nums1, nums2);
 * obj.add(index,val);
 * int param_2 = obj.count(tot);
 */

public class Solution extends BaseSolution {


    @Override
    public Object solve(String[] inputJsonValues) {
        String[] operators = jsonArrayToStringArray(inputJsonValues[0]);
		String[][] opValues = jsonArrayToString2DArray(inputJsonValues[1]);
		int[] nums1 = jsonArrayToIntArray(opValues[0][0]);
		int[] nums2 = jsonArrayToIntArray(opValues[0][1]);
		FindSumPairs obj = new FindSumPairs(nums1, nums2);
		List<Object> ans = new ArrayList<>(operators.length);
		ans.add(null);
		for (int i = 1; i < operators.length; i++) {
			if (operators[i].compareTo("add") == 0) {
				int index = Integer.parseInt(opValues[i][0]);
				int val = Integer.parseInt(opValues[i][1]);
				obj.add(index, val);
				ans.add(null);
				continue;
			}
			if (operators[i].compareTo("count") == 0) {
				int tot = Integer.parseInt(opValues[i][0]);
				ans.add(obj.count(tot));
				continue;
			}
			ans.add(null);
		}
        return JSON.toJSON(ans);
    }
}
