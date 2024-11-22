package problems.problems_LCR_113;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int numCourses = Integer.parseInt(inputJsonValues[0]);
		int[][] prerequisites = jsonArrayToInt2DArray(inputJsonValues[1]);
        return JSON.toJSON(findOrder(numCourses, prerequisites));
    }
}
