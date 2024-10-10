package problems.problems_3162;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int numberOfPairs(int[] nums1, int[] nums2, int k) {
        Map<Integer, Integer> counter = new HashMap<>();
        for (int num: nums1) {
            if (num % k != 0) {
                continue;
            }
            num /= k;
            for (int i = 1; i * i <= num; i++) {
                if (num % i != 0) {
                    continue;
                }
                counter.put(i, counter.getOrDefault(i, 0) + 1);
                if (i * i != num) {
                    counter.put(num / i, counter.getOrDefault(num / i, 0) + 1);
                }
            }
        }
        int ans = 0;
        for (int num: nums2) {
            ans += counter.getOrDefault(num, 0);
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums1 = jsonArrayToIntArray(inputJsonValues[0]);
		int[] nums2 = jsonArrayToIntArray(inputJsonValues[1]);
		int k = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(numberOfPairs(nums1, nums2, k));
    }
}
