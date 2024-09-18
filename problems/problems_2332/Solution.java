package problems.problems_2332;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int latestTimeCatchTheBus(int[] buses, int[] passengers, int capacity) {
        Arrays.sort(buses);
        Arrays.sort(passengers);
        int n = passengers.length;
        int j = 0, c = 0;
        for (int bus: buses) {
            c = capacity;
            while (c > 0 && j < n && passengers[j] <= bus) {
                c--;
                j++;
            }
        }
        j--;
        int ans = c > 0 ? buses[buses.length - 1] : passengers[j];
        while (j >= 0 && ans == passengers[j]) {
            j--;
            ans--;
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] buses = jsonArrayToIntArray(inputJsonValues[0]);
		int[] passengers = jsonArrayToIntArray(inputJsonValues[1]);
		int capacity = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(latestTimeCatchTheBus(buses, passengers, capacity));
    }
}
