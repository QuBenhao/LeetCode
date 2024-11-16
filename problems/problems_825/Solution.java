package problems.problems_825;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int numFriendRequests(int[] ages) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] ages = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(numFriendRequests(ages));
    }
}
