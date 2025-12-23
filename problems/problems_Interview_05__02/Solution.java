package problems.problems_Interview_05__02;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String printBin(double num) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        double num = Double.parseDouble(inputJsonValues[0]);
        return JSON.toJSON(printBin(num));
    }
}
