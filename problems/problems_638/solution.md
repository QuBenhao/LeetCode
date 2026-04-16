# [Python/Java/JavaScript] DFS

> Author: Benhao
> Date: 2021-10-24
> Upvotes: 19
> Tags: Java, JavaScript, Python, Python3

---

### 解题思路
终于能写熟悉的DFS了

### 代码

```Python3 []
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        @lru_cache(None)
        def dfs(remains):
            ans = sum(r*price[i] for i,r in enumerate(remains))
            if ans:
                for ssp in special:
                    check = True
                    for i in range(len(remains)):
                        if ssp[i] > remains[i]:
                            check = False
                            break
                    if check:
                        new = list(remains)
                        for i in range(len(remains)):
                            new[i] -= ssp[i]
                        ans = min(ans, dfs(tuple(new)) + ssp[-1])
            return ans
        
        return dfs(tuple(needs))
```
```Java []
class Solution {
    List<Integer> price;
    List<List<Integer>> special;
    Map<String, Integer> cache;
    public int shoppingOffers(List<Integer> price_, List<List<Integer>> special_, List<Integer> needs) {
        price = price_;
        special = special_;
        cache = new HashMap<>();
        return dfs(needs);
    }

    private int dfs(List<Integer> needs){
        int ans = 0;
        StringBuilder sb = new StringBuilder();
        for(int i=0;i<needs.size();i++){
            ans += price.get(i) * needs.get(i);
            sb.append(needs.get(i) + "#");
        }
        if(ans != 0){
            String key = sb.toString();
            if(cache.containsKey(key)){
                ans = cache.get(key);
            }else{
                for(List<Integer> sp: special){
                    boolean check = true;
                    for(int i=0;i<needs.size();i++)
                        if(sp.get(i) > needs.get(i)){
                            check = false;
                            break;
                        }
                    if(check){
                        List<Integer> next = new ArrayList<>();
                        for(int i=0;i<needs.size();i++){
                            next.add(needs.get(i) - sp.get(i));
                        }
                        ans = Math.min(ans, dfs(next) + sp.get(sp.size()-1));
                    }
                }
                cache.put(key, ans);
            }
        }
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {number[]} price
 * @param {number[][]} special
 * @param {number[]} needs
 * @return {number}
 */
var shoppingOffers = function(price, special, needs) {
    const cache = new Map();

    const dfs = (remain) => {
        let ans = 0;
        for(let i=0;i<remain.length;i++)
            ans += price[i] * remain[i];
        if(ans != 0){
            const key = remain.join("#");
            if(cache.has(key))
                ans = cache.get(key);
            else{
                for(const sp of special){
                    let check = true;
                    for(let i=0;i<remain.length;i++)
                        if(sp[i] > remain[i]){
                            check = false;
                            break;
                        }
                    if(check){
                        const next = [];
                        for(let i=0;i<remain.length;i++)
                            next.push(remain[i] - sp[i]);
                        ans = Math.min(ans, dfs(next) + sp[sp.length-1]);
                    }
                }
                cache.set(key, ans);
            }
        }
        return ans;
    }

    return dfs(needs);
};
```