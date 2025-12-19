package problems.problems_Interview_16__03;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public double[] intersection(int[] start1, int[] end1, int[] start2, int[] end2) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] start1 = jsonArrayToIntArray(inputJsonValues[0]);
		int[] end1 = jsonArrayToIntArray(inputJsonValues[1]);
		int[] start2 = jsonArrayToIntArray(inputJsonValues[2]);
		int[] end2 = jsonArrayToIntArray(inputJsonValues[3]);
        return JSON.toJSON(intersection(start1, end1, start2, end2));
    }
}
