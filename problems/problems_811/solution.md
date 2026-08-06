# [Python/Java/TypeScript/Go] 哈希表模拟

> slug: pythonjavatypescriptgo-mo-ni-by-himymben-b87j
> date: 2022-10-05
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Subdomain Visit Count (subdomain-visit-count)
> url: https://leetcode.cn/problems/subdomain-visit-count/solutions/Q8zpPU/pythonjavatypescriptgo-mo-ni-by-himymben-b87j/

---
### 解题思路
按题目对每个域名统计次数，最终返回即可

### 代码

```python3 []
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = Counter()
        for s in cpdomains:
            sp = s.split()
            cnts, idx = int(sp[0]), -1
            while idx < len(sp[1]):
                counter[sp[1][idx + 1:]] += cnts
                idx = sp[1].find(".", idx + 1)
                if idx == -1:
                    break
        return [f"{v} {k}" for k, v in counter.items()]
```
```Java []
class Solution {
    public List<String> subdomainVisits(String[] cpdomains) {
        Map<String, Integer> map = new HashMap<>();
        for (String s: cpdomains) {
            String[] sp = s.split(" ");
            int cnts = Integer.parseInt(sp[0]), idx = -1;
            while (idx < sp[1].length()) {
                String tmp = sp[1].substring(idx + 1);
                map.put(tmp, map.getOrDefault(tmp, 0) + cnts);
                idx = sp[1].indexOf(".", idx + 1);
                if (idx == -1) {
                    break;
                }
            }
        }
        final List<String> ans = new ArrayList<>();
        map.forEach((k, v) -> {
            ans.add(v + " " + k);
        });
        return ans;
    }
}
```
```TypeScript []
function subdomainVisits(cpdomains: string[]): string[] {
    const ans: Array<string> = new Array<string>(), map: Map<string, number> = new Map<string, number>()
    for (const s of cpdomains) {
        const sp: Array<string> = s.split(" ")
        const cnts: number = Number.parseInt(sp[0])
        let idx: number = -1
        while (true) {
            const sub: string = sp[1].substring(idx + 1)
            map.set(sub, (map.get(sub) | 0) + cnts)
            idx = sp[1].indexOf(".", idx + 1)
            if (idx == -1) {
                break
            }
        }
    }
    map.forEach((val, key) => {
        ans.push(val + " " + key)
    })
    return ans
};
```
```Go []
func subdomainVisits(cpdomains []string) []string {
    ans, mp := []string{}, map[string]int{}
    for _, s := range cpdomains {
        sp := strings.Split(s, " ")
        cnts, _ := strconv.Atoi(sp[0])
        idx := -1
        for true {
            sp[1] = sp[1][idx + 1:]
            mp[sp[1]] += cnts
            idx = strings.Index(sp[1], ".")
            if idx == -1 {
                break
            }
        }
    }
    for k, v := range mp {
        ans = append(ans, strconv.Itoa(v) + " " + k)
    }
    return ans
}
```