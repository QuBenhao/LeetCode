package problems.problems_1061;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


class UnionFind {
    private final int[] parent;
    private final int[] size;
    private int count;

    public UnionFind(int size) {
        parent = new int[size];
        this.size = new int[size];
        for (int i = 0; i < size; i++) {
            parent[i] = i;
            this.size[i] = 1; // Initialize size of each component to 1
        }
        count = size; // Initially, each element is its own component
    }

    public int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]); // Path compression
        }
        return parent[x];
    }

    public boolean union(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX == rootY) {
            return false; // Already in the same component
        }

        int fa = Math.min(rootX, rootY), child = Math.max(rootX, rootY);
        parent[child] = fa; // Union by rank
        size[fa] += size[child]; // Update size of the new root
        count--; // Decrease the number of components
        return true;
    }
}


public class Solution extends BaseSolution {
    public String smallestEquivalentString(String s1, String s2, String baseStr) {
        UnionFind uf = new UnionFind(26);
        for (int i = 0; i < s1.length(); i++) {
            uf.union(s1.charAt(i) - 'a', s2.charAt(i) - 'a');
        }

        StringBuilder result = new StringBuilder();
        for (char c : baseStr.toCharArray()) {
            int root = uf.find(c - 'a');
            result.append((char) (root + 'a'));
        }
        return result.toString();
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s1 = jsonStringToString(inputJsonValues[0]);
		String s2 = jsonStringToString(inputJsonValues[1]);
		String baseStr = jsonStringToString(inputJsonValues[2]);
        return JSON.toJSON(smallestEquivalentString(s1, s2, baseStr));
    }
}
