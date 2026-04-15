# [Python/Java/JavaScript/Go] 数组模拟

> Author: Benhao
> Date: 2022-03-17
> Upvotes: 19
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
直接按题意模拟即可

### 代码

```Python3 []
class Bank:

    def __init__(self, balance: List[int]):
        self.b, self.n = balance, len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 <= self.n and account2 <= self.n and self.b[account1 - 1] >= money:
            self.b[account1 - 1] -= money
            self.b[account2 - 1] += money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if account <= self.n:
            self.b[account - 1] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if account <= self.n and self.b[account - 1] >= money:
            self.b[account - 1] -= money
            return True
        return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
```
```Java []
class Bank {
    private long[] b;
    public Bank(long[] balance) {
        b = balance;
    }
    
    public boolean transfer(int account1, int account2, long money) {
        if(account1 <= b.length && account2 <= b.length && b[account1 - 1] >= money) {
            b[account1 - 1] -= money;
            b[account2 - 1] += money;
            return true;
        }
        return false;
    }
    
    public boolean deposit(int account, long money) {
        if(account <= b.length) {
            b[account - 1] += money;
            return true;
        }
        return false;
    }
    
    public boolean withdraw(int account, long money) {
        if(account <= b.length && b[account - 1] >= money) {
            b[account - 1] -= money;
            return true;
        }
        return false;
    }
}

/**
 * Your Bank object will be instantiated and called as such:
 * Bank obj = new Bank(balance);
 * boolean param_1 = obj.transfer(account1,account2,money);
 * boolean param_2 = obj.deposit(account,money);
 * boolean param_3 = obj.withdraw(account,money);
 */
```
```JavaScript []
/**
 * @param {number[]} balance
 */
var Bank = function(balance) {
    this.b = balance
};

/** 
 * @param {number} account1 
 * @param {number} account2 
 * @param {number} money
 * @return {boolean}
 */
Bank.prototype.transfer = function(account1, account2, money) {
    if(account1 <= this.b.length && account2 <= this.b.length && this.b[account1 - 1] >= money) {
        this.b[account1 - 1] -= money
        this.b[account2 - 1] += money
        return true
    }
    return false
};

/** 
 * @param {number} account 
 * @param {number} money
 * @return {boolean}
 */
Bank.prototype.deposit = function(account, money) {
    if(account <= this.b.length) {
        this.b[account - 1] += money
        return true
    }
    return false
};

/** 
 * @param {number} account 
 * @param {number} money
 * @return {boolean}
 */
Bank.prototype.withdraw = function(account, money) {
    if(account <= this.b.length && this.b[account - 1] >= money) {
        this.b[account - 1] -= money
        return true
    }
    return false
};

/**
 * Your Bank object will be instantiated and called as such:
 * var obj = new Bank(balance)
 * var param_1 = obj.transfer(account1,account2,money)
 * var param_2 = obj.deposit(account,money)
 * var param_3 = obj.withdraw(account,money)
 */
```
```Go []
type Bank struct {
    B []int64
}


func Constructor(balance []int64) Bank {
    return Bank{balance}
}


func (this *Bank) Transfer(account1 int, account2 int, money int64) bool {
    if account1 <= len(this.B) && account2 <= len(this.B) && this.B[account1 - 1] >= money {
        this.B[account1 - 1] -= money
        this.B[account2 - 1] += money
        return true
    }
    return false
}


func (this *Bank) Deposit(account int, money int64) bool {
    if account <= len(this.B) {
        this.B[account - 1] += money
        return true
    }
    return false
}


func (this *Bank) Withdraw(account int, money int64) bool {
    if account <= len(this.B) && this.B[account - 1] >= money {
        this.B[account - 1] -= money
        return true
    }
    return false
}


/**
 * Your Bank object will be instantiated and called as such:
 * obj := Constructor(balance);
 * param_1 := obj.Transfer(account1,account2,money);
 * param_2 := obj.Deposit(account,money);
 * param_3 := obj.Withdraw(account,money);
 */
```