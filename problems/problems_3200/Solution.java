package problems.problems_3200;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxHeightOfTriangle(int red, int blue) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int red = Integer.parseInt(inputJsonValues[0]);
		int blue = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(maxHeightOfTriangle(red, blue));
    }
}
