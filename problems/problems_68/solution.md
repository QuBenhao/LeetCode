# [Python/Java] 硬模拟

> Author: Benhao
> Date: 2021-09-08
> Upvotes: 10
> Tags: Java, Python, Python3

---

### 解题思路
统计哪些单词构成一行以后，将该行进行左右对齐的空格补齐。

### 代码

```Python3 []
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # 将word[left]到word[right-1]的单词组合成一个左右对齐的行
        def process(left, right):
            # 结尾行，向后补齐空格
            if right == n:
                res = ' '.join(words[left:right])
                res += ' ' * (maxWidth - len(res))
                return res
            spaces = right - left - 1
            # 单独单词构成的行，向后补齐空格
            if not spaces:
                return words[left] + ' ' * (maxWidth - len(words[left]))
            cur = sum(len(w) for w in words[left:right]) + spaces
            # 统计每个空隙间的空格数
            each = [1] * spaces
            j = 0
            while cur < maxWidth:
                # 根据题意优先补左边，所以从0开始
                each[j] += 1
                j += 1
                if j == spaces:
                    j = 0
                cur += 1
            j = 0
            res = ''
            # 根据每个间隙的空格数构建该行字符串
            while left < right:
                res += words[left]
                if left < right - 1:
                    res += ' ' * each[j]
                    j += 1
                left += 1
            return res

        n = len(words)
        idx = i = 0
        ans = []
        while idx < n:
            i = idx
            curLen = len(words[idx])
            idx += 1
            # 统计哪些单词组成一行
            while idx < n and curLen < maxWidth:
                # 单词之间需要空格
                curLen += 1
                curLen += len(words[idx])
                idx += 1
            if curLen > maxWidth:
                idx -= 1
                curLen -= len(words[idx]) + 1
            ans.append(process(i, idx))
        return ans
```
```Java []
class Solution {
    String[] words;
    int maxWidth, n;
    public List<String> fullJustify(String[] w, int m) {
        words = w;
        maxWidth = m;
        n = w.length;
        List<String> ans = new ArrayList<>();
        for(int idx = 0;idx < n;){
            int start = idx, len = words[idx++].length();
            while(idx < n && len < maxWidth)
                len += words[idx++].length() + 1;
            if(len > maxWidth)
                len -= words[--idx].length() + 1;
            ans.add(process(start, idx));            
        }
        return ans;
    }

    public String process(int from, int to){
        StringBuilder sb = new StringBuilder();
        if(to == n || to == from + 1){
            while(from < to){
                sb.append(words[from++]);
                if(from < to) sb.append(' ');
            }
            while(sb.length() < maxWidth)
                sb.append(' ');
            return sb.toString();
        }
        int spaces = to - from - 1;
        int cur = spaces, j = 0;
        for(int i=from;i<to;i++)
            cur += words[i].length();
        int[] each = new int[spaces];
        Arrays.fill(each, 1);
        while(cur++ < maxWidth){
            each[j++]+=1;
            if(j==spaces) j = 0;
        }
        j = 0;
        while(from < to){
            sb.append(words[from++]);
            if(from < to)
                for(int i=0;i<each[j];i++)
                    sb.append(' ');
            j++;
        }
        return sb.toString();
    }
}
```