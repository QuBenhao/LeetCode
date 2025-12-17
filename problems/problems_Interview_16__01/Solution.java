package problems.problems_Interview_16__01;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] swapNumbers(int[] numbers) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] numbers = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(swapNumbers(numbers));
    }
}
