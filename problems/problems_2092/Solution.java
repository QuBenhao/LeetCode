package problems.problems_2092;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<Integer> findAllPeople(int n, int[][] meetings, int firstPerson) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int[][] meetings = jsonArrayToInt2DArray(inputJsonValues[1]);
		int firstPerson = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(findAllPeople(n, meetings, firstPerson));
    }
}
