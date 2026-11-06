package problems.problems_1882;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] assignTasks(int[] servers, int[] tasks) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] servers = jsonArrayToIntArray(inputJsonValues[0]);
		int[] tasks = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(assignTasks(servers, tasks));
    }
}
