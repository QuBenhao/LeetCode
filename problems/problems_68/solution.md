# [Python/Java] Direct simulation

> Author: Benhao
> Date: 2021-09-08
> Upvotes: 10
> Tags: Java, Python, Python3

---

### Approach
After determining which words fit on a line, pad the line with spaces to justify both margins.

### Code

```Python3 []
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # Combine words from word[left] through word[right-1] into a fully justified line
        def process(left, right):
            # Pad the final line with trailing spaces
            if right == n:
                res = ' '.join(words[left:right])
                res += ' ' * (maxWidth - len(res))
                return res
            spaces = right - left - 1
            # Pad a single-word line with trailing spaces
            if not spaces:
                return words[left] + ' ' * (maxWidth - len(words[left]))
            cur = sum(len(w) for w in words[left:right]) + spaces
            # Calculate the number of spaces in each gap
            each = [1] * spaces
            j = 0
            while cur < maxWidth:
                # The problem requires filling gaps on the left first, so start at 0
                each[j] += 1
                j += 1
                if j == spaces:
                    j = 0
                cur += 1
            j = 0
            res = ''
            # Build the line using the number of spaces in each gap
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
            # Determine which words form one line
            while idx < n and curLen < maxWidth:
                # Spaces are required between words
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
