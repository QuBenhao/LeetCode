package problems.problems_691;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minStickers(String[] stickers, String target) {
        Set<Character> targetSet = new HashSet<Character>();
        for(int i = 0; i < target.length(); i++)
            targetSet.add(target.charAt(i));
        List<Map<Character, Integer>> available = new ArrayList<>();
        for(String s: stickers) {
            Map<Character, Integer> map = getCounter(s, targetSet);
            if(map != null) {
                available.add(map);
            }
        }
        Deque<String> queue = new ArrayDeque<>();
        queue.addLast(target);
        Map<String, Integer> cost = new HashMap<>();
        cost.put(target, 0);
        while(!queue.isEmpty()) {
            String cur = queue.pollFirst();
            for(Map<Character, Integer> map: available) {
                if(map.containsKey(cur.charAt(0))) {
                    String nxt = nextState(cur, new HashMap<>(map));
                    if(nxt.length() == 0) {
                        return cost.get(cur) + 1;
                    } else if(!cost.containsKey(nxt)) {
                        cost.put(nxt, cost.get(cur) + 1);
                        queue.addLast(nxt);
                    }
                }
            }
        }
        return -1;
    }

    private Map<Character, Integer> getCounter(String s, Set<Character> chars) {
        Map<Character, Integer> map = new HashMap<>();
        for(int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if(chars.contains(c)) {
                map.put(c, map.getOrDefault(c, 0) + 1);
            }
        }
        return map.size() > 0 ? map : null;
    }

    private String nextState(String s, Map<Character, Integer> map) {
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if(map.getOrDefault(c, 0) > 0) {
                map.put(c, map.get(c) - 1);
            } else {
                sb.append(c);
            }
        }
        return sb.toString();
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String[] stickers = jsonArrayToStringArray(inputJsonValues[0]);
		String target = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(minStickers(stickers, target));
    }
}
