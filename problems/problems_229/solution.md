# [Python/Java/JavaScript] Simulation -> generalized Boyer-Moore majority vote

> slug: pythonjavajavascript-mo-ni-by-himymben-abvt
> date: 2021-10-21
> tags: Java, JavaScript, Python, Python3
> question: Majority Element II (majority-element-ii)
> url: https://leetcode.cn/problems/majority-element-ii/solutions/I2v6eM/pythonjavajavascript-mo-ni-by-himymben-abvt/

---
### Approach
We previously used Boyer-Moore majority voting to find a number occurring more than half the time. The idea here is the same, except that three different values cancel each other instead of two.
Likewise, to find values occurring more than $\lfloor \frac{n}{k} \rfloor$ times, cancel groups of $k$ different values.

At most $\lfloor \frac{n}{k} \rfloor$ groups of $k$ values can be canceled, so a value occurring more often must remain.

### Code

```python3
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        return [k for k,v in Counter(nums).items() if v > len(nums)//3]
```

```Python3 []
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Boyer-Moore majority vote: cancel each group of three different values
        numA = numB = None
        cntA = cntB = 0
        for num in nums:
            if num == numA:
                cntA += 1
            elif num == numB:
                cntB += 1
            elif numA is None:
                numA = num
                cntA += 1
            elif numB is None:
                numB = num
                cntB += 1
            else:
                cntA -= 1
                cntB -= 1
                if not cntA:
                    numA = None
                if not cntB:
                    numB = None
        # Verify the counts
        cntA = cntB = 0
        for num in nums:
            if num == numA:
                cntA += 1
            elif num == numB:
                cntB += 1
        s = len(nums)//3
        ans = []
        if cntA > s:
            ans.append(numA)
        if cntB > s:
            ans.append(numB)
        return ans
```
```Java []
class Solution {
    public List<Integer> majorityElement(int[] nums) {
        int numA = Integer.MIN_VALUE, numB = Integer.MIN_VALUE;
        int cntA = 0, cntB = 0;
        for(int num:nums){
            if(num == numA)
                cntA++;
            else if(num == numB)
                cntB++;
            else if(numA == Integer.MIN_VALUE){
                numA = num;
                cntA++;
            }else if(numB == Integer.MIN_VALUE){
                numB = num;
                cntB++;
            }else{
                cntA--;
                cntB--;
                if(cntA==0)
                    numA = Integer.MIN_VALUE;
                if(cntB==0)
                    numB = Integer.MIN_VALUE;
            }
        }
        cntA = cntB = 0;
        for(int num:nums){
            if(num == numA)
                cntA++;
            else if(num == numB)
                cntB++;
        }
        List<Integer> ans = new ArrayList<>();
        int s = nums.length/3;
        if(cntA > s)
            ans.add(numA);
        if(cntB > s)
            ans.add(numB);
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var majorityElement = function(nums) {
    let numA = undefined, numB = undefined;
    let cntA = 0, cntB = 0;
    for(const num of nums){
        if(num === numA)
            cntA++;
        else if(num === numB)
            cntB++;
        else if(numA === undefined){
            numA = num;
            cntA++;
        }else if(numB == undefined){
            numB = num;
            cntB++;
        }else{
            cntA--;
            cntB--;
            if(cntA==0)
                numA = undefined;
            if(cntB==0)
                numB = undefined;
        }
    }
    cntA = cntB = 0;
    for(const num of nums){
        if(num == numA)
            cntA++;
        else if(num == numB)
            cntB++;
    }
    const ans = [];
    const s = Math.floor(nums.length/3);
    if(cntA > s)
        ans.push(numA);
    if(cntB > s)
        ans.push(numB);
    return ans;
};
```

Generalized Boyer-Moore majority vote for k (can still be optimized)
```Python3
k = 3
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        major = [[0, None] for i in range(k - 1)]
        for num in nums:
            exist, idx = False, None
            for i in range(k - 1):
                if not major[i][0] and idx is None:
                    idx = i
                if num == major[i][1]:
                    major[i][0] += 1
                    exist = True
                    break
            if not exist:
                if idx is not None:
                    major[idx][0] += 1
                    major[idx][1] = num
                else:
                    for i in range(k - 1):
                        major[i][0] -= 1
        checks = dict()
        for items in major:
            if items[0]:
                checks[items[1]] = 0
        for num in nums:
            if num in checks:
                checks[num] += 1
        s = len(nums) // k
        return [k for k,v in checks.items() if v > s]
```
