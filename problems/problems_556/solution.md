# [Python/Java/TypeScript/Go] Next permutation

> Author: Benhao
> Date: 2022-07-03
> Upvotes: 9
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### Approach
This is essentially the next-permutation problem, with some boundary issues.
I took a shortcut and reused my code for problem 31 as a helper function.

Here is a simple example.
To find the next permutation of 1111169741, scan from right to left for the first break in increasing order, between 9 and 6.
Swap 6 with the first digit greater than 6 in 1479, keeping the next permutation as small as possible. This gives 1111179641.
Reverse the 9641 suffix to get 1111171469.

### Code

```Python3 []
MAX_32 = 2147483647
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        return nxt if (nxt := int("".join(map(str, self.nextPermutation(list(map(int, list(str(n))))))))) > n and nxt <= MAX_32 else -1

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        index = -1
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                index = i
                break

        if index == -1:
            nums.reverse()
            return nums

        for i in range(n-1,index,-1):
            if nums[i] > nums[index]:
                nums[i], nums[index] = nums[index], nums[i]
                break

        left, right = index + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        return nums
```
```Java []
class Solution {
    public int nextGreaterElement(int n) {
        List<Integer> nums = intToList(n);
        int index = -1, len = nums.size();
        for (int i = 1; i < len; i++) {
            if (nums.get(i) < nums.get(i - 1)) {
                index = i;
                break;
            }
        }
        if (index == -1) {
            return -1;
        }
        for (int i = 0; i < index; i++) {
            if (nums.get(i) > nums.get(index)) {
                swap(nums, index, i);
                break;
            }
        }
        for (int left = 0, right = index - 1; left < right; left++, right--) {
            swap(nums, left, right);
        }
        return listToInt(nums);
    }

    private void swap(List<Integer> list, int i, int j) {
        int tmp = list.get(i);
        list.set(i, list.get(j));
        list.set(j, tmp);
    }

    private List<Integer> intToList(int n) {
        List<Integer> ans = new ArrayList<>();
        while (n > 0) {
            ans.add(n % 10);
            n /= 10;
        }
        return ans;
    }

    private int listToInt(List<Integer> nums) {
        long ans = 0;
        for (int i = nums.size() - 1; i >= 0; i--) {
            ans = 10 * ans + nums.get(i);
        }
        return ans > Integer.MAX_VALUE ? -1 : (int)ans;
    }
}
```
```TypeScript []
const MAX = 2147483647
function nextGreaterElement(n: number): number {
    const numberToArray = (x: number): Array<number> => {
        const arr = new Array<number>()
        while (x > 0) {
            arr.push(x % 10)
            x = Math.floor(x / 10)
        }
        return arr
    }, arrayToNum = (arr: Array<number>): number => {
        let ans = 0
        for (let i = arr.length - 1; i >= 0; i--) {
            ans = 10 * ans + arr[i]
        }
        return ans > MAX ? -1 : ans
    }, swap = (arr: Array<number>, i: number, j: number): void => {
        const tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
    }

    const nums = numberToArray(n)
    const len = nums.length
    let index = -1
    for (let i = 1; i < len; i++) {
        if (nums[i] < nums[i - 1]) {
            index = i
            break
        }
    }
    if (index == -1) {
        return -1
    }
    for (let i = 0; i < index; i++) {
        if (nums[i] > nums[index]) {
            swap(nums, index, i)
            break
        }
    }
    for (let left = 0, right = index - 1; left < right; left++, right--) {
        swap(nums, left, right)
    }
    return arrayToNum(nums)
};
```
```Go []
const MAX = 2147483647
func nextGreaterElement(n int) int {
    numToArray := func (x int) (ans []int) {
        for ; x > 0; x /= 10 {
            ans = append(ans, x % 10)
        }
        return
    }
    arrayToNum := func (arr []int) (ans int) {
        for i := len(arr) - 1; i >= 0; i-- {
            ans = ans * 10 + arr[i]
        }
        if ans > MAX {
            return -1
        }
        return 
    }
    nums := numToArray(n)
    index := -1
    for i := 1; i < len(nums); i++ {
        if nums[i] < nums[i - 1] {
            index = i
            break
        }
    }
    if index == -1 {
        return -1
    }
    for i := 0; i < index; i++ {
        if nums[i] > nums[index] {
            nums[i], nums[index] = nums[index], nums[i]
            break
        }
    }
    for left, right := 0, index - 1; left < right; left++ {
        nums[left], nums[right] = nums[right], nums[left]
        right--
    }
    return arrayToNum(nums)
}
```
