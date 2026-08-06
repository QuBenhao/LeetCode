# [Python/Java/TypeScript/Go] 模拟

> slug: pythonjavatypescriptgo-mo-ni-by-himymben-yjxt
> date: 2022-06-28
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Encode and Decode TinyURL (encode-and-decode-tinyurl)
> url: https://leetcode.cn/problems/encode-and-decode-tinyurl/solutions/2mnY3Z/pythonjavatypescriptgo-mo-ni-by-himymben-yjxt/

---
### 解题思路
这题就按题意找一个方式实现就好。我个人其实是倾向于用rsa非对称加密的，密钥用短一点的生成的固长就不会特别长，不过没有导入这个库。

### 代码

```Python3 []
import hashlib
class Codec:
    def __init__(self):
        self.map = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        _md5 = hashlib.md5()
        _md5.update(longUrl.encode("utf-8"))
        res = _md5.hexdigest()
        self.map[res] = longUrl
        return f"http://tinyurl.com/{res}"
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.map[shortUrl.split("/")[-1]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
```
```Java []
public class Codec {

    private volatile AtomicInteger idx = new AtomicInteger();
    private Map<Integer, String> map = new HashMap<>();

    // Encodes a URL to a shortened URL.
    public String encode(String longUrl) {
        int cur = idx.getAndIncrement();
        map.put(cur, longUrl);
        return String.format("http://tinyurl.com/%d", cur);
    }

    // Decodes a shortened URL to its original URL.
    public String decode(String shortUrl) {
        String[] sp = shortUrl.split("/");
        return map.get(Integer.parseInt(sp[sp.length - 1]));
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(url));
```
```TypeScript []
const map = new Map<string, string>(), chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

/**
 * Encodes a URL to a shortened URL.
 */
function encode(longUrl: string): string {
    const s = randomStr()
    map.set(s, longUrl)
    // console.log(s)
    return "http://tinyurl.com/" + s
};

/**
 * Decodes a shortened URL to its original URL.
 */
function decode(shortUrl: string): string {
	const sp = shortUrl.split("/")
    return map.get(sp[sp.length - 1])
};

/**
 * Your functions will be called as such:
 * decode(encode(strs));
 */
let count = 0, len = 6
function randomStr(): string {
    const res = []
    for (let i = 0; i < len; i++) {
        res.push(chars.charAt(Math.floor(Math.random() * chars.length)))
    }
    const s = res.join("")
    if(map.has(s)) {
        count++
        if(count == 3) {
            len += 2
            count = 0
        }
        return randomStr()
    }
    return s
}
```
```Go []
type Codec struct {
    Idx int
    Map map[int]string
}


func Constructor() Codec {
    return Codec{100000, map[int]string{}}
}

// Encodes a URL to a shortened URL.
func (this *Codec) encode(longUrl string) string {
	this.Map[this.Idx] = longUrl
    this.Idx++
    return "http://tinyurl.com/" + strconv.Itoa(this.Idx - 1)
}

// Decodes a shortened URL to its original URL.
func (this *Codec) decode(shortUrl string) string {
    sp := strings.Split(shortUrl, "/")
    idx, _ := strconv.Atoi(sp[len(sp) - 1])
    return this.Map[idx]
}


/**
 * Your Codec object will be instantiated and called as such:
 * obj := Constructor();
 * url := obj.encode(longUrl);
 * ans := obj.decode(url);
 */
```