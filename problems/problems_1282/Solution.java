package problems.problems_1282;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<List<Integer>> groupThePeople(int[] groupSizes) {
        Map<Integer, List<Integer>> groups = new HashMap<>();
        for (int i = 0; i < groupSizes.length; i++) {
            int size = groupSizes[i];
            groups.putIfAbsent(size, new ArrayList<>());
            groups.get(size).add(i);
        }
        List<List<Integer>> result = new ArrayList<>();
        for (var entry : groups.entrySet()) {
            int size = entry.getKey();
            List<Integer> groupList = entry.getValue();
            for (int i = 0; i < groupList.size(); i += size) {
                result.add(new ArrayList<>(groupList.subList(i, i + size)));
            }
        }
        return result;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] groupSizes = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(groupThePeople(groupSizes));
    }
}
