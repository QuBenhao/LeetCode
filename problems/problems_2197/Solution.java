package problems.problems_2197;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<Integer> replaceNonCoprimes(int[] nums) {
        List<Integer> ans = new ArrayList<>();
        for (int num: nums) {
            while (!ans.isEmpty()) {
                int g = gcd(num, ans.getLast());
                if (g == 1) {
                    break;
                }
                num = ans.removeLast() / g * num;
            }
            ans.add(num);
        }
        return ans;
    }
    
    private int gcd(int a, int b) {
        while (a != 0) {
            int tmp = a;
            a = b % a;
            b = tmp;
        }
        return b;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(replaceNonCoprimes(nums));
    }
}
