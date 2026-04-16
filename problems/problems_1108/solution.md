# [Python/Java/JavaScript/TypeScript/Go] ?

> Author: Benhao
> Date: 2022-06-20
> Upvotes: 13
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
emmm

### 代码

```Python3 []
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")
```
```Java []
class Solution {
    public String defangIPaddr(String address) {
        return address.replace(".", "[.]");
    }
}
```
```JavaScript []
/**
 * @param {string} address
 * @return {string}
 */
var defangIPaddr = function(address) {
    return address.replaceAll(".", "[.]")
};
```
```TypeScript []
function defangIPaddr(address: string): string {
    return address.split(".").join("[.]")
};
```
```Go []
func defangIPaddr(address string) string {
    return strings.ReplaceAll(address, ".", "[.]")
}
```