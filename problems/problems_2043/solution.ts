class Bank {
    constructor(balance: number[]) {
        
    }

    transfer(account1: number, account2: number, money: number): boolean {
        
    }

    deposit(account: number, money: number): boolean {
        
    }

    withdraw(account: number, money: number): boolean {
        
    }
}

/**
 * Your Bank object will be instantiated and called as such:
 * var obj = new Bank(balance)
 * var param_1 = obj.transfer(account1,account2,money)
 * var param_2 = obj.deposit(account,money)
 * var param_3 = obj.withdraw(account,money)
 */

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const operators: string[] = JSON.parse(inputValues[0]);
	const opValues: any[][] = JSON.parse(inputValues[1]);
	const ans: any[] = [null];
	const obj: Bank = new Bank(opValues[0][0]);
	for (let i: number = 1; i < operators.length; i++) {
		if (operators[i] == "transfer") {
			ans.push(obj.transfer(opValues[i][0], opValues[i][1], opValues[i][2]));
			continue;
		}
		if (operators[i] == "deposit") {
			ans.push(obj.deposit(opValues[i][0], opValues[i][1]));
			continue;
		}
		if (operators[i] == "withdraw") {
			ans.push(obj.withdraw(opValues[i][0], opValues[i][1]));
			continue;
		}
		ans.push(null);
	}
	return ans;
}
