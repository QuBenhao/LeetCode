package problems.problems_1103;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] distributeCandies(int candies, int num_people) {
        double f = Math.sqrt(candies * 2);
        int x = (int)f + 1, s;
        for (s = x * (x + 1) / 2; s > candies; x--) {
            s -= x;
        }
        int remain = candies - s, div = x / num_people, mod = x % num_people;
        int[] ans = new int[num_people];
        for (int i = 0; i < num_people; i++) {
            ans[i] = (i + 1) * div + num_people * div * (div - 1) / 2;
            if (i < mod) {
                ans[i] += num_people * div + i + 1;
            }
        }
        ans[mod] += remain;
        return ans;
    }

    @Override
    public Object solve(String[] values) {
        int candies = Integer.parseInt(values[0]);
		int num_people = Integer.parseInt(values[1]);
        return JSON.toJSON(distributeCandies(candies, num_people));
    }
}
