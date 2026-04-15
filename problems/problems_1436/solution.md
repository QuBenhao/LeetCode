# [Python/Java] 统计只在右边出现过一次的城市

> Author: Benhao
> Date: 2021-09-30
> Upvotes: 9
> Tags: Java, Python, Python3

---

```Python3 []
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        return (set((city:=list(zip(*paths)))[1]) - set(city[0])).pop()
```
```Java []
class Solution {
    public String destCity(List<List<String>> paths) {
        Set<String> cityA = new HashSet<>(), cityB = new HashSet<>();
        for(List<String> path: paths){
            cityA.add(path.get(0));
            cityB.add(path.get(1));
        }
        for(String city: cityB)
            if(!cityA.contains(city))
                return city;
        return null;
    }
}
```