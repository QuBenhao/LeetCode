# [Python/Java/TypeScript/Go] 模拟

> slug: pythonjavajavascriptgo-by-himymben-5i56
> date: 2022-05-29
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Validate IP Address (validate-ip-address)
> url: https://leetcode.cn/problems/validate-ip-address/solutions/MHPa5v/pythonjavajavascriptgo-by-himymben-5i56/

---
### 解题思路
根据'.'和':'判断是IPv4还是IPv6。
根据判断IPv4规则，按'.'分割字符串后需要长度为4，且分割的每个字符串长度在1到3之间，可以解析为数字，不含前导零然后大小在0到255之间。
根据判断IPv6规则，按':'分割字符串后需要长度为8，且分割的每个字符串长度在1到4之间，每个字符都需要在0-9或a-f或A-F中。

### 代码

```Python3 []
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def isIPv4(ip: str) -> bool:
            return all(s and s.isdigit() and not(s[0] == '0' and len(s) > 1) and 0 <= int(s) <= 255 for s in sp) if len(sp := ip.split(".")) == 4 else False
        
        def isIPv6(ip: str) -> bool:
            return all(s and len(s) <= 4 and all(c in "0123456789ABCDEFabcdef" for c in s) for s in sp) if len(sp := ip.split(":")) == 8 else False

        if "." in queryIP and ":" not in queryIP and isIPv4(queryIP):
            return "IPv4"
        elif ":" in queryIP and "." not in queryIP and isIPv6(queryIP):
            return "IPv6"
        return "Neither"
```
```Java []
class Solution {
    private static final String IPv6_CHARS = "0123456789abcdefABCDEF";
    public String validIPAddress(String queryIP) {
        boolean isIPv4 = queryIP.indexOf(".") >= 0, isIPv6 = queryIP.indexOf(":") >= 0;
        if(isIPv4 && !isIPv6) {
            if (checkIPv4(queryIP)) {
                return "IPv4";
            }
        } else if(isIPv6 && !isIPv4) {
            if (checkIPv6(queryIP)) {
                return "IPv6";
            }
        }
        return "Neither";
    }

    private boolean checkIPv4(String ip) {
        String[] splits = ip.split("\\.");
        if(splits.length != 4 || ip.charAt(0) == '.' || ip.charAt(ip.length() - 1) == '.') {
            return false;
        }
        for(String s: splits) {
            if (s.length() > 3 || s.length() == 0 || (s.length() > 1 && s.charAt(0) == '0')) {
                return false;
            }
            int cur = 0;
            for(int i = 0; i < s.length(); i++) {
                if('0' <= s.charAt(i) && s.charAt(i) <= '9') {
                    cur = 10 * cur + s.charAt(i) - '0';
                } else {
                    return false;
                }
            }
            if (cur > 255) {
                return false;
            }
        }
        return true;
    }

    private boolean checkIPv6(String ip) {
        String[] splits = ip.split("\\:");
        if(splits.length != 8 || ip.charAt(0) == ':' || ip.charAt(ip.length() - 1) == ':') {
            return false;
        }
        for(String s:splits) {
            if (s.length() > 4 || s.length() == 0) {
                return false;
            }
            for(int i = 0; i < s.length(); i++) {
                if(IPv6_CHARS.indexOf(s.charAt(i)) == -1) {
                    return false;
                }
            }
        }
        return true;
    }
}
```
```TypeScript []
function validIPAddress(queryIP: string): string {
    const isIPv4 = queryIP.indexOf(".") >= 0, isIPv6 = queryIP.indexOf(":") >= 0
    if (isIPv4 && !isIPv6) {
        if (IPv4Check(queryIP)) {
            return "IPv4"
        }
    } else if (isIPv6 && !isIPv4) {
        if (IPv6Check(queryIP)) {
            return "IPv6"
        }
    }
    return "Neither";
};

function IPv4Check(ip: string): boolean {
    const splits = ip.split(".")
    if (splits.length != 4) {
        return false
    }
    for (const s of splits) {
        if (s.length > 3 || s.length == 0 || (s.length > 1 && s.charCodeAt(0) == '0'.charCodeAt(0))) {
            return false
        }
        let cur = 0
        for (let i = 0; i < s.length; i++) {
            if (s.charCodeAt(i) <= '9'.charCodeAt(0) && s.charCodeAt(i) >= '0'.charCodeAt(0)) {
                cur = 10 * cur + s.charCodeAt(i) - '0'.charCodeAt(0)
            } else {
                return false
            }
        }
        if (cur > 255) {
            return false
        }
    }
    return true
};

function IPv6Check(ip: string): boolean {
    const splits = ip.split(":")
    if (splits.length != 8) {
        return false
    }
    for (const s of splits) {
        if (s.length > 4 || s.length == 0) {
            return false
        }
        for (let i = 0; i < s.length; i++) {
            const c = s.charCodeAt(i)
            if (! (('0'.charCodeAt(0) <= c && c <= '9'.charCodeAt(0)) || ('a'.charCodeAt(0) <= c && 'f'.charCodeAt(0) >= c) || ('A'.charCodeAt(0) <= c && c <= 'F'.charCodeAt(0)))) {
                return false
            }
        }
    }
    return true
}
```
```Go []
func validIPAddress(queryIP string) string {
    isIPv4, isIPv6 := strings.Contains(queryIP, "."), strings.Contains(queryIP, ":")
    if isIPv4 && !isIPv6 && ipv4Check(queryIP) {
        return "IPv4"
    }
    if isIPv6 && !isIPv4 && ipv6Check(queryIP) {
        return "IPv6"
    }
    return "Neither"
}

func ipv4Check(ip string) bool {
    if sp := strings.Split(ip, "."); len(sp) == 4 {
        for _, s := range sp {
            if len(s) > 3 || len(s) == 0 || (len(s) > 1 && s[0] == '0') {
                return false
            }
            if v, err := strconv.Atoi(s); err != nil || v > 255 {
                return false
            }
        }
        return true
    } else {
        return false
    }
}

func ipv6Check(ip string) bool {
    if sp := strings.Split(ip, ":"); len(sp) == 8 {
        for _, s := range sp {
            if len(s) > 4 || len(s) == 0 {
                return false
            }
            if _, err := strconv.ParseUint(s, 16, 64); err != nil {
                return false
            }
        }
        return true
    } else {
        return false
    }
}
```