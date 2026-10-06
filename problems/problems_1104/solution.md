# [Python/Java] Two very simple recurrence formulas (both metrics beat 100%)

> Author: Benhao
> Date: 2021-07-28
> Upvotes: 4
> Tags: Java, Python, Python3

---

### Approach
I call the endpoint where a level begins the entry endpoint, and the endpoint leading into the next level the exit endpoint.
Each level's entry endpoint is $2^n$, and its exit endpoint is $2^{n+1}-1$.
**A node's distance from its level's entry endpoint, divided by 2**, equals **its parent's distance from the previous level's exit endpoint**.
Or:
**A node's distance from its level's exit endpoint, divided by 2**, equals **its parent's distance from the previous level's entry endpoint**.

$x = 2^n + k, y = 2^n - 1 - k/2$, where $x$ is the node and $y$ is its parent.

> For example, in the first example, the distance from 14 to its entry endpoint 8 is 6. Its parent's distance from the exit endpoint of the preceding level is therefore 3, giving 7-3=4.
The distance from 4 to 4 is 0, so the next node is 3-0=3, and so on.
This follows from the labeling of the binary tree and the fact that every level has twice as many nodes as the preceding level.
The parent's distance from the endpoint on the same side is simply the current node's distance scaled down by a factor of 2.


### Code
Scale toward the smaller endpoint
```python3 []
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        ans = [label]
        # Initial entry endpoint
        last = 2 ** int(log(label, 2))
        while label > 1:
            # The parent node's distance from its exit endpoint
            add = label - last >> 1
            # Calculate the parent node's value 
            label = last - 1 - add
            # The next entry endpoint is half the current one
            last >>= 1
            ans.append(label)
        return ans[::-1]
```
```python3 []
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        # Find the greatest power of 2 less than or equal to x: the entry endpoint
        def closest(x):
            if not x & (x-1):
                return x
            x -= 1
            x |= x>>1
            x |= x>>2
            x |= x>>4
            x |= x>>8
            x |= x>>16
            return x + 1 >> 1 if x >= 0 else 1

        ans = [label]
        # Initial entry endpoint
        last = closest(label)
        while label > 1:
            # The parent node's distance from its exit endpoint
            add = label - last >> 1
            # Calculate the parent node's value 
            label = last - 1 - add
            # The next entry endpoint is half the current one
            last >>= 1
            ans.append(label)
        return ans[::-1]

```
```java []
class Solution {
    public List<Integer> pathInZigZagTree(int label) {
        ArrayList<Integer> ans = new ArrayList<>();
        ans.add(label);
        int last = closest(label);
        while(label > 1){
            int add = label - last >> 1;
            label = last - 1 - add;
            last >>= 1;
            ans.add(label);
        }
        Collections.reverse(ans);
        return ans;
    }

    public int closest(int x){
        if((x & (x-1))==0)
            return x;
        x--;
        x |= x >>> 1;
        x |= x >>> 2;
        x |= x >>> 4;
        x |= x >>> 8;
        x |= x >>> 16;
        if (x >= 0)
            return x + 1 >> 1;
        return 1;
    }
}
```

Scale toward the larger endpoint
```python3 []
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        ans = [label]
        # Initial exit endpoint
        last = 2 ** (int(log(label, 2)) + 1)
        while label > 1:
            # The parent node's distance from its entry endpoint
            dis = last - 1 - label >> 1
            # Calculate the parent node's value 
            label = last//4 + dis
            # The next exit endpoint is obtained by dividing by 2
            last >>= 1
            ans.append(label)
        return ans[::-1]
```
```python3 []
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        # Find the smallest power of 2 greater than x to obtain the exit endpoint
        def closest(x):
            if not x & (x-1):
                x += 1
            x -= 1
            x |= x>>1
            x |= x>>2
            x |= x>>4
            x |= x>>8
            x |= x>>16
            return x + 1 if x >= 0 else 1

        ans = [label]
        # Initial exit endpoint
        last = closest(label)
        while label > 1:
            # The parent node's distance from its entry endpoint
            dis = last - 1 - label >> 1
            # Calculate the parent node's value 
            label = last//4 + dis
            # The next exit endpoint is obtained by dividing by 2
            last >>= 1
            ans.append(label)
        return ans[::-1]
```
```java []
class Solution {
    public List<Integer> pathInZigZagTree(int label) {
        ArrayList<Integer> ans = new ArrayList<>();
        ans.add(label);
        int last = closest(label);
        while(label > 1){
            int dis = last - 1 - label >> 1;
            last >>= 1;
            label = (last/2) + dis;
            ans.add(label);
        }
        Collections.reverse(ans);
        return ans;
    }

    public int closest(int x){
        if((x & (x-1))==0)
            x++;
        x--;
        x |= x >>> 1;
        x |= x >>> 2;
        x |= x >>> 4;
        x |= x >>> 8;
        x |= x >>> 16;
        if (x >= 0)
            return x + 1;
        return 1;
    }
}
```
