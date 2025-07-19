package problems.problems_1233;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<String> removeSubfolders(String[] folder) {
        List<String> result = new ArrayList<>();
        Arrays.sort(folder);
        String last = "#";
        for (String f : folder) {
            if (!f.startsWith(last)) {
                result.add(f);
                last = f + "/";
            }
        }
        return result;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String[] folder = jsonArrayToStringArray(inputJsonValues[0]);
        return JSON.toJSON(removeSubfolders(folder));
    }
}
