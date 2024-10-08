package problems.problems_1436;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String destCity(List<List<String>> paths) {
        Set<String> cities = new HashSet<>();
        for (List<String> path : paths) {
            cities.add(path.get(0));
        }
        for (List<String> path : paths) {
            if (!cities.contains(path.get(1))) {
                return path.get(1);
            }
        }
        return "";
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        List<List<String>> paths = jsonArrayToString2DList(inputJsonValues[0]);
        return JSON.toJSON(destCity(paths));
    }
}
