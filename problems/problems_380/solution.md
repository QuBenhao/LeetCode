# [Python/Java/JavaScript/Go] 哈希表

> slug: pythonjavajavascriptgo-by-himymben-nlrg
> date: 2022-04-12
> tags: Go, Java, JavaScript, Python, Python3
> question: Insert Delete GetRandom O(1) (insert-delete-getrandom-o1)
> url: https://leetcode.cn/problems/insert-delete-getrandom-o1/solutions/rBsOj7/pythonjavajavascriptgo-by-himymben-nlrg/

---
### 解题思路
核心思想：
1. 哈希表记录加入和删除的数，可以O(1)检查是否出现过
2. 用数组维护所有数，方便随机取一个数，数组后加入一个数也是O(1)，唯一难点在于删除。
3. 用哈希表维护每个数加入时的坐标，在要删除的数不是数组最后一个时，与最后一个交换（因为是不在乎顺序的，所以这种交换不影响任何东西），此时要删除的数成为数组最后一个，可以O(1)删除

### 代码

```Python3 []
class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.idx_map = dict()

    def insert(self, val: int) -> bool:
        if val not in self.idx_map:
            self.idx_map[val] = len(self.nums)
            self.nums.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.idx_map:
            swap_val, idx = self.nums[-1], self.idx_map[val]
            self.nums[idx] = swap_val
            self.idx_map[swap_val] = idx
            del self.idx_map[val]
            self.nums.pop()
            return True
        return False

    def getRandom(self) -> int:
        return choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
```
```Java []
class RandomizedSet {
    private List<Integer> nums;
    private Map<Integer, Integer> idxMap;
    private Random random;
    public RandomizedSet() {
        nums = new ArrayList<>();
        idxMap = new HashMap<>();
        random = new Random();
    }
    
    public boolean insert(int val) {
        if(!idxMap.containsKey(val)) {
            idxMap.put(val, nums.size());
            nums.add(val);
            return true;
        }
        return false;
    }
    
    public boolean remove(int val) {
        if(idxMap.containsKey(val)) {
            int swapVal = nums.get(nums.size() - 1), idx = idxMap.get(val);
            idxMap.put(swapVal, idx);
            nums.set(idx, swapVal);
            idxMap.remove(val);
            nums.remove(nums.size() - 1);
            return true;
        }
        return false;
    }
    
    public int getRandom() {
        int randomIdx = random.nextInt(nums.size());
        return nums.get(randomIdx);
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
```
```JavaScript []
var RandomizedSet = function() {
    this.map = new Map()
    this.nums = new Array()
};

/** 
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.insert = function(val) {
    if(!this.map.has(val)) {
        this.map.set(val, this.nums.length)
        this.nums.push(val)
        return true
    }
    return false
};

/** 
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.remove = function(val) {
    if(this.map.has(val)) {
        const swapVal = this.nums[this.nums.length - 1], idx = this.map.get(val)
        this.nums[idx] = swapVal
        this.map.set(swapVal, idx)
        this.map.delete(val)
        this.nums.pop()
        return true
    }
    return false
};

/**
 * @return {number}
 */
RandomizedSet.prototype.getRandom = function() {
    const randomIdx = Math.floor(Math.random() * this.nums.length);
    return this.nums[randomIdx];
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * var obj = new RandomizedSet()
 * var param_1 = obj.insert(val)
 * var param_2 = obj.remove(val)
 * var param_3 = obj.getRandom()
 */
```
```Go []
type RandomizedSet struct {
    IdxMap map[int]int
    Nums []int
}


func Constructor() RandomizedSet {
    return RandomizedSet{map[int]int{}, []int{}}
}


func (this *RandomizedSet) Insert(val int) bool {
    if _, ok := this.IdxMap[val]; !ok {
        this.IdxMap[val] = len(this.Nums)
        this.Nums = append(this.Nums, val)
        return true
    }
    return false
}


func (this *RandomizedSet) Remove(val int) bool {
    if idx, ok := this.IdxMap[val]; ok {
        swapVal := this.Nums[len(this.Nums) - 1]
        this.Nums[idx] = swapVal
        this.IdxMap[swapVal] = idx
        delete(this.IdxMap, val)
        this.Nums = this.Nums[:len(this.Nums) - 1]
        return true
    }
    return false
}


func (this *RandomizedSet) GetRandom() int {
    randomIdx := rand.Intn(len(this.Nums))
    return this.Nums[randomIdx]
}


/**
 * Your RandomizedSet object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Insert(val);
 * param_2 := obj.Remove(val);
 * param_3 := obj.GetRandom();
 */
```