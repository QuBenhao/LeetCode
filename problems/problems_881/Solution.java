package problems.problems_881;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);
        int ans = 0;
        for (int left = 0, right = people.length - 1; left <= right; right--, ans++) {
            if (people[left] + people[right] <= limit) {
                left++;
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] values) {
        int[] people = jsonArrayToIntArray(values[0]);
		int limit = Integer.parseInt(values[1]);
        return JSON.toJSON(numRescueBoats(people, limit));
    }
}
