package problems.problems_1948;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<List<String>> deleteDuplicateFolder(List<List<String>> paths) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        List<List<String>> paths = jsonArrayToString2DList(inputJsonValues[0]);
        return JSON.toJSON(deleteDuplicateFolder(paths));
    }
}
