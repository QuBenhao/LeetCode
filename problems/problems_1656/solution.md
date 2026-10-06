# [Python/Java/TypeScript/Go] Simulation

> Author: Benhao
> Date: 2022-08-15
> Upvotes: 17
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### Approach
I found the statement confusing, but implemented its instructions directly.

The insertion position is fixed by the index. The return value depends on the current ptr; advance ptr only when inserting at ptr.

### Code

```Python3 []
class OrderedStream:

    def __init__(self, n: int):
        self.data, self.ptr = [None] * n, 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.data[idKey - 1] = value
        ans = []
        while self.ptr < len(self.data) and self.data[self.ptr]:
            ans.append(self.data[self.ptr])
            self.ptr += 1
        return ans

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
```
```Java []
class OrderedStream {
    private String[] data;
    private int ptr;
    public OrderedStream(int n) {
        data = new String[n];
        ptr = 0;
    }
    
    public List<String> insert(int idKey, String value) {
        data[--idKey] = value;
        List<String> ans = new ArrayList<>();
        while (ptr < data.length && data[ptr] != null) {
            ans.add(data[ptr++]);
        }
        return ans;
    }
}

/**
 * Your OrderedStream object will be instantiated and called as such:
 * OrderedStream obj = new OrderedStream(n);
 * List<String> param_1 = obj.insert(idKey,value);
 */
```
```TypeScript []
class OrderedStream {
    ptr: number
    data: Array<string>
    constructor(n: number) {
        this.ptr = 0
        this.data = new Array<string>(n)
    }

    insert(idKey: number, value: string): string[] {
        this.data[--idKey] = value
        const ans: Array<string> = new Array<string>()
        while (this.ptr < this.data.length && this.data[this.ptr] !== undefined) {
            ans.push(this.data[this.ptr++])
        }
        return ans
    }
}

/**
 * Your OrderedStream object will be instantiated and called as such:
 * var obj = new OrderedStream(n)
 * var param_1 = obj.insert(idKey,value)
 */
```
```Go []
type OrderedStream struct {
    Data []string
    Ptr int
}


func Constructor(n int) OrderedStream {
    return OrderedStream{make([]string, n), 0}
}


func (this *OrderedStream) Insert(idKey int, value string) (ans []string) {
    idKey--
    this.Data[idKey] = value
    for this.Ptr < len(this.Data) && this.Data[this.Ptr] != "" {
        ans = append(ans, this.Data[this.Ptr])
        this.Ptr++
    }
    return
}


/**
 * Your OrderedStream object will be instantiated and called as such:
 * obj := Constructor(n);
 * param_1 := obj.Insert(idKey,value);
 */
```
