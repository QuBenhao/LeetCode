package problems.problems_1233;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<String> removeSubfolders(String[] folder) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String[] folder = jsonArrayToStringArray(inputJsonValues[0]);
        return JSON.toJSON(removeSubfolders(folder));
    }
}
