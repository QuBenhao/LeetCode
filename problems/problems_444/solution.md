# [Python/Java/TypeScript/Go] Simulation

> slug: -by-himymben-d0lm
> date: 2022-07-23
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Sequence Reconstruction (sequence-reconstruction)
> url: https://leetcode.cn/problems/sequence-reconstruction/solutions/umaDnF/-by-himymben-d0lm/

---
### Approach
Check whether every adjacent relationship appears. The reconstruction is unique only if all of them do.

### Code

```Python3 []
class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        return len(edges := {(a, b) for seq in sequences for a,b in pairwise(seq)}) >= 0 and all((a, b) in edges for a, b in pairwise(nums))
```
```Java []
class Solution {
    public boolean sequenceReconstruction(int[] nums, int[][] sequences) {
        Set<Integer> set = new HashSet<>();
        for (int[] seq: sequences) {
            for (int i = 0; i < seq.length - 1; i++) {
                set.add(hash(seq[i], seq[i + 1]));
            }
        }
        for (int i = 0; i < nums.length - 1; i++) {
            if (!set.contains(hash(nums[i], nums[i + 1]))) {
                return false;
            }
        }
        return true;
    }

    private int hash(int prev, int next) {
        // 10^4 requires at most 14 bits
        return prev << 14 | next;
    }
}
```
```TypeScript []
function sequenceReconstruction(nums: number[], sequences: number[][]): boolean {
    const hash = (prev: number, next: number): number => {
        return prev << 14 | next
    }
    const s = new Set<number>()
    for (const seq of sequences) {
        for (let i = 0; i < seq.length - 1; i++) {
            s.add(hash(seq[i], seq[i + 1]))
        }
    }
    for (let i = 0; i < nums.length - 1; i++) {
        if (!s.has(hash(nums[i], nums[i + 1]))) {
            return false
        }
    }
    return true
};
```
```Go []
func sequenceReconstruction(nums []int, sequences [][]int) bool {
    hash := func(prev, next int) int {
        return prev << 14 | next
    }
    set := map[int]bool{}
    for _, seq := range sequences {
        for i := 0; i < len(seq) - 1; i++ {
            set[hash(seq[i], seq[i + 1])] = true
        }
    }
    for i := 0; i < len(nums) - 1; i++ {
        if !set[hash(nums[i], nums[i + 1])] {
            return false
        }
    }
    return true
}
```
