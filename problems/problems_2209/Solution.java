package problems.problems_2209;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minimumWhiteTiles(String floor, int numCarpets, int carpetLen) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String floor = jsonStringToString(inputJsonValues[0]);
		int numCarpets = Integer.parseInt(inputJsonValues[1]);
		int carpetLen = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(minimumWhiteTiles(floor, numCarpets, carpetLen));
    }
}
