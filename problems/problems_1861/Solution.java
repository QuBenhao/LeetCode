package problems.problems_1861;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public char[][] rotateTheBox(char[][] boxGrid) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        char[][] boxGrid = jsonArrayToChar2DArray(inputJsonValues[0]);
        return JSON.toJSON(rotateTheBox(boxGrid));
    }
}
