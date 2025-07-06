package problems.problems_3607;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] processQueries(int c, int[][] connections, int[][] queries) {
        UnionFind uf = new UnionFind(c);
        for (int[] connection : connections) {
            uf.union(connection[0] - 1, connection[1] - 1);
        }

        Map<Integer, DoubleLinkedNode> nodeMap = new HashMap<>(c);
        Map<Integer, DoubleLinkedNode> rootMap = new HashMap<>(uf.getCount());
        for (int i = 0; i < c; ++i) {
            int root = uf.find(i);
            if (!rootMap.containsKey(root)) {
                DoubleLinkedNode head = new DoubleLinkedNode(-1);
                head.next = head;
                head.prev = head;
                rootMap.put(root, head);
            }
            DoubleLinkedNode node = new DoubleLinkedNode(i+1);
            rootMap.get(root).prev.insertAfter(node);
            nodeMap.put(i, node);
        }

        List<Integer> results = new ArrayList<>();
        for (int[] query : queries) {
            int op = query[0], x = query[1] - 1;
            int root = uf.find(x);
            if (op == 2) {
                if (nodeMap.containsKey(x)) {
                    DoubleLinkedNode node = nodeMap.get(x);
                    node.remove();
                    nodeMap.remove(x);
                }
            } else {
                DoubleLinkedNode rootHead = rootMap.get(root);
                if (rootHead.next == rootHead) {
                    results.add(-1);
                } else {
                    DoubleLinkedNode node;
                    if (nodeMap.containsKey(x)) {
                        node = nodeMap.get(x);
                    } else {
                        node = rootHead.next;
                    }
                    results.add(node.val);
                }
            }
        }
        return results.stream().mapToInt(i -> i).toArray();
    }

    class DoubleLinkedNode {
        int val;
        DoubleLinkedNode prev;
        DoubleLinkedNode next;

        public DoubleLinkedNode(int val) {
            this.val = val;
            this.prev = null;
            this.next = null;
        }

        public void insertAfter(DoubleLinkedNode node) {
            node.prev = this;
            node.next = this.next;
            this.next.prev = node;
            this.next = node;
        }

        public void remove() {
            this.prev.next = this.next;
            this.next.prev = this.prev;
            this.prev = null;
            this.next = null;
        }
    }

    class UnionFind {
        private final int[] parent;
        private final int[] size;
        private int count;

        public UnionFind(int n) {
            parent = new int[n];
            size = new int[n];
            count = n;
            for (int i = 0; i < n; i++) {
                parent[i] = i;
                size[i] = 1;
            }
        }

        public int find(int x) {
            if (parent[x] != x) {
                parent[x] = find(parent[x]); // Path compression
            }
            return parent[x];
        }

        public boolean union(int x, int y) {
            int px = find(x);
            int py = find(y);
            if (px == py) {
                return false; // Already in the same set
            }
            if (size[px] < size[py]) {
                parent[px] = py;
                size[py] += size[px];
            } else {
                parent[py] = px;
                size[px] += size[py];
            }
            count--;
            return true; // Union successful
        }

        public int getCount() {
            return count;
        }
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int c = Integer.parseInt(inputJsonValues[0]);
		int[][] connections = jsonArrayToInt2DArray(inputJsonValues[1]);
		int[][] queries = jsonArrayToInt2DArray(inputJsonValues[2]);
        return JSON.toJSON(processQueries(c, connections, queries));
    }
}
