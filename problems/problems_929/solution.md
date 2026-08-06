# [Python/Java/TypeScript/Go] 模拟

> slug: pythonjavatypescriptgo-mo-ni-by-himymben-clem
> date: 2022-06-04
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Unique Email Addresses (unique-email-addresses)
> url: https://leetcode.cn/problems/unique-email-addresses/solutions/vBHiCA/pythonjavatypescriptgo-mo-ni-by-himymben-clem/

---
### 解题思路
将简化后的地址加入哈希表中统计即可

### 代码

```Python3 []
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        return len(set(sp[0].split("+")[0].replace(".", "") + "@" + sp[1] if (sp := email.split("@")) else "" for email in emails))
```
```Java []
class Solution {
    public int numUniqueEmails(String[] emails) {
        Set<String> set = new HashSet<>();
        for(String email: emails) {
            String[] sp = email.split("@");
            String localName = sp[0].split("\\+")[0].replaceAll("\\.", "");
            set.add(localName + "@" + sp[1]);
        } 
        return set.size();
    }
}
```
```TypeScript []
function numUniqueEmails(emails: string[]): number {
    const s = new Set()
    for(const email of emails) {
        const sp = email.split("@")
        const localName = sp[0].split("+")[0].split(".").join("")
        s.add(localName + "@" + sp[1])
    }
    return s.size
};
```
```Go []
func numUniqueEmails(emails []string) int {
    set := map[string]bool{}
    for _, email := range emails {
        sp := strings.Split(email, "@")
        localName := strings.ReplaceAll(strings.Split(sp[0], "+")[0], ".", "")
        set[localName + "@" + sp[1]] = true
    }
    return len(set)
}
```