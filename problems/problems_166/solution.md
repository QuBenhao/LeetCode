# [Python/Java/JavaScript] 高精度除法模板

> Author: Benhao
> Date: 2021-10-03
> Upvotes: 17
> Tags: Java, JavaScript, Python, Python3

---

### 解题思路
每一位小数是通过*10再除余计算的。而循环小数我们可以通过判断被除数有没有出现过，出现的位置在哪儿来判断(哈希记录)

### 代码

```Python3 []
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        def hdiv(dividend, divisor, precision=0):
            a = dividend  
            b = divisor
            #有负数的话做个标记  
            if (a > 0 and b > 0) or (a < 0 and b < 0):  
                flag = 1  
            else:  
                flag = -1 
            
            #变为正数，防止取模的时候有影响  
            a = abs(a)  
            b = abs(b)  
        
            quotient = a // b  
            remainder = a % b  
            
            if remainder == 0:  
                return str(quotient * flag)
            
            ans = [str(quotient), '.']
            repeats = dict()
            i = 0  
            while i < precision:  
                a = remainder * 10  
                quotient = a // b  
                remainder = a % b
                if a in repeats:
                    ans.insert(repeats[a], '(')
                    ans.append(')')
                    break
                ans.append(str(quotient))
                repeats[a] = i + 2
                if remainder == 0:  
                    break  
                i += 1  
            
            if precision == 0:  
                ans.pop(1)

            if flag == -1:  
                return '-' + ''.join(ans) 
            
            return ''.join(ans)
        
        return hdiv(numerator, denominator, 10000)
```
```Java []
class Solution {
    public String fractionToDecimal(int numerator, int denominator) {
        long a = numerator, b = denominator;
        int flag = 1;
        if((a < 0 && b > 0) || (a>0 && b<0)) flag = -1;
        a = Math.abs(a);
        b = Math.abs(b);
        long quotient = a / b;
        long remainder = a % b;
        if(remainder == 0)
            return String.valueOf(quotient * flag);
        StringBuilder sb = new StringBuilder(String.valueOf(quotient));
        sb.append('.');
        int len = sb.length();
        Map<Long, Integer> repeats = new HashMap<>();
        for(int i=0; i<10000; i++){
            a = remainder * 10;
            quotient = a / b;
            remainder = a % b;
            if(repeats.containsKey(a)){
                sb.insert((int)repeats.get(a), '(');
                sb.append(')');
                break;
            }
            sb.append(String.valueOf(quotient));
            repeats.put(a, i + len);
            if(remainder == 0)
                break;
        }
        if(flag == -1)
            return "-" + sb.toString();
        return sb.toString();        
    }
}
```
```JavaScript []
/**
 * @param {number} numerator
 * @param {number} denominator
 * @return {string}
 */
var fractionToDecimal = function(numerator, denominator) {
    let flag = 1;
    if((numerator < 0 && denominator > 0) || (numerator > 0 && denominator < 0))
        flag = -1;
    numerator = Math.abs(numerator);
    denominator = Math.abs(denominator);
    let quotient = Math.floor(numerator / denominator);
    let remainder = numerator % denominator;
    if(remainder == 0)
        return "" + quotient * flag;
    const ans = [];
    ans.push(quotient.toString());
    ans.push('.');
    const repeats = new Map();
    for(let i=0; i<10000; i++){
        numerator = remainder * 10;
        quotient = Math.floor(numerator / denominator);
        remainder = numerator % denominator;
        if(repeats.has(numerator)){
            ans.splice(repeats.get(numerator), 0, '(');
            ans.push(')');
            break;
        }
        ans.push(quotient.toString());
        repeats.set(numerator, i + 2);
        if(remainder == 0)
            break;
    }
    if(flag == -1)
        return "-" + ans.join("");
    return ans.join("");       
};
```