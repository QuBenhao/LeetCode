# [Python] Greedy Manhattan distance

> Author: Benhao
> Date: 2021-08-21
> Upvotes: 11
> Tags: Java, Python, Python3

---

```Python3 []
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        # Heuristic: reaching the target takes at least abs(targetX - 0) + abs(targetY - 0) steps
        # Enemies can move freely; if any enemy can reach the target by then, we cannot reach it safely
        # To see why, if an enemy can catch us along the way, it can also follow our remaining path and reach the target at the same time
        # Only a fool would think taking more steps (a detour) could avoid the enemy; that merely gives it more time to reach the target
        def manhattanDistance(p1, p2):
            return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])
        m = manhattanDistance((0, 0), target)
        return all(manhattanDistance(g, target) > m for g in ghosts)
```
```Java []
class Solution {
    public boolean escapeGhosts(int[][] ghosts, int[] target) {
        int m = manhattanDistance(new int[]{0, 0}, target);
        for(int i=0;i<ghosts.length;i++)
            if(m >= manhattanDistance(ghosts[i], target))
                return false;
        return true;
    }

    public int manhattanDistance(int[] point1, int[] point2){
        return Math.abs(point1[0] - point2[0]) + Math.abs(point1[1] - point2[1]);
    }
}
```
