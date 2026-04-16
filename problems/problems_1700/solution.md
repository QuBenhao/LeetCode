# [Python/Java/TypeScript/Go] 模拟

> Author: Benhao
> Date: 2022-10-19
> Upvotes: 4
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
不在乎学生的顺序，只要还有喜欢某种三明治的学生，就可以走下去

### 代码

```Python3 []
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnts = Counter(students)
        for sw in sandwiches:
            if not cnts[sw]:
                break
            cnts[sw] -= 1
        return cnts[0] + cnts[1]
```
```Java []
class Solution {
    public int countStudents(int[] students, int[] sandwiches) {
        Map<Integer, Integer> map = new HashMap<>(2);
        for (int st: students) {
            map.put(st, map.getOrDefault(st, 0) + 1);
        }
        for (int sw: sandwiches) {
            if (map.getOrDefault(sw, 0) == 0) {
                break;
            }
            map.put(sw, map.get(sw) - 1);
        }
        return map.getOrDefault(0, 0) + map.getOrDefault(1, 0);
    }
}
```
```TypeScript []
function countStudents(students: number[], sandwiches: number[]): number {
    const mp: Map<number, number> = new Map<number, number>()
    for (const st of students) {
        mp.set(st, (mp.get(st) | 0) + 1)
    }
    for (const sw of sandwiches) {
        if ((mp.get(sw) | 0) == 0) {
            break
        }
        mp.set(sw, mp.get(sw) - 1)
    }
    return (mp.get(0) | 0) + (mp.get(1) | 0)
};
```
```Go []
func countStudents(students []int, sandwiches []int) int {
    mp := map[int]int{}
    for _, st := range students {
        mp[st]++
    }
    for _, sw := range sandwiches {
        if mp[sw] == 0 {
            break
        }
        mp[sw]--
    }
    return mp[0] + mp[1]
}
```