class ATM {
    constructor() {
        
    }

    deposit(banknotesCount: number[]): void {
        
    }

    withdraw(amount: number): number[] {
        
    }
}

/**
 * Your ATM object will be instantiated and called as such:
 * var obj = new ATM()
 * obj.deposit(banknotesCount)
 * var param_2 = obj.withdraw(amount)
 */

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const operators: string[] = JSON.parse(inputValues[0]);
	const opValues: any[][] = JSON.parse(inputValues[1]);
	const ans: any[] = [null];
	const obj: ATM = new ATM();
	for (let i: number = 1; i < operators.length; i++) {
		if (operators[i] == "deposit") {
			obj.deposit(opValues[i][0]);
			ans.push(null);
			continue;
		}
		if (operators[i] == "withdraw") {
			ans.push(obj.withdraw(opValues[i][0]));
			continue;
		}
		ans.push(null);
	}
	return ans;
}
