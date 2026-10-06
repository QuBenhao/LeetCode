# [Python] Prefix sums + binary search for a random number

> Author: Benhao
> Date: 2021-08-29
> Upvotes: 19
> Tags: Java, Python, Python3

---

### Approach
The problem may be hard to understand. In plain terms, imagine a very large array containing w[i] copies of each index i, then choose one entry at random.
This interpretation gives code like the following, but uses a lot of space. Here we generate 10000 random choices in advance.
```python3
class Solution:

    def __init__(self, w: List[int]):
        total = sum(w)
        self.list = [i for i in range(len(w))]
        self.weight = [0] * len(w)
        for i,num in enumerate(w):
            self.weight[i] += float(num/total)
        self.picks = random.choices(self.list, self.weight, k=10000)
        self.idx = -1

    def pickIndex(self) -> int:
        self.idx += 1
        return self.picks[self.idx]
```
How can we generate the choices more efficiently?

If the first index has $k_0$ copies, it occupies $[1,k_0]$. If the second has $k_1$ copies, it occupies $[k_0+1,k_0+k_1]$. A random number in $[1,k_0+k_1]$ falls in the first interval with probability $\frac{k_0}{k_0+k_1}$, exactly as required.
Binary search maps this random number back to the original index. A value at most $k_0$ maps to index 0, a value greater than $k_0$ and less than $k_1$ maps to index 1, and so on. We therefore only need to generate one random number.

### Code

```Python3 []
class Solution:

    def __init__(self, w: List[int]):
        # Compute prefix sums to map a random number to the index of its weighted interval
        self.presum = list(accumulate(w))

    def pickIndex(self) -> int:
        rand = random.randint(1, self.presum[-1])
        return bisect_left(self.presum, rand)
```
```Java []
class Solution {
    Random r = new Random();
    int n;
    int[] presum;
    public Solution(int[] w) {
        n = w.length;
        presum = w;
        for(int i=1;i<n;i++)
            presum[i] += presum[i-1];
    }
    
    public int pickIndex() {
        int rand = r.nextInt(presum[n-1]) + 1;
        return binarySearch(rand);
    }

    public int binarySearch(int x){
        int left = 0, right = n - 1;
        while(left < right){
            int mid = (left + right)/2;
            if(presum[mid] >= x)
                right = mid;
            else
                left = mid + 1;
        }
        return left;
    }
}
```
