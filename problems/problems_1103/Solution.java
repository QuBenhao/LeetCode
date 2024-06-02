package problems.problems_1103;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] distributeCandies(int candies, int num_people) {

    }

    @Override
    public Object solve(String[] values) {
        int candies = Integer.parseInt(values[0]);
		int num_people = Integer.parseInt(values[1]);
        return JSON.toJSON(distributeCandies(candies, num_people));
    }
}
