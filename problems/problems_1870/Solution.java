package problems.problems_1870;

import com.alibaba.fastjson.JSON;

import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minSpeedOnTime(int[] dist, double hour) {
        int n = dist.length;
        if (hour <= n - 1) {
            return -1;
        }
        int l = 1, r = 10000000;
        while (l < r) {
            int mid = (l + r) / 2;
            double time = 0;
            for (int i = 0; i < n - 1; i++) {
                time += (dist[i] + mid - 1) / mid;
            }
            time += (double) dist[n - 1] / mid;
            if (time <= hour) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return l;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] dist = jsonArrayToIntArray(inputJsonValues[0]);
		double hour = Double.parseDouble(inputJsonValues[1]);
        return JSON.toJSON(minSpeedOnTime(dist, hour));
    }
}
