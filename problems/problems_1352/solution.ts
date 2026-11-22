class ProductOfNumbers {
    constructor() {
        
    }

    add(num: number): void {
        
    }

    getProduct(k: number): number {
        
    }
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * var obj = new ProductOfNumbers()
 * obj.add(num)
 * var param_2 = obj.getProduct(k)
 */

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const operators: string[] = JSON.parse(inputValues[0]);
	const opValues: any[][] = JSON.parse(inputValues[1]);
	const ans: any[] = [null];
	const obj: ProductOfNumbers = new ProductOfNumbers();
	for (let i: number = 1; i < operators.length; i++) {
		if (operators[i] == "add") {
			obj.add(opValues[i][0]);
			ans.push(null);
			continue;
		}
		if (operators[i] == "getProduct") {
			ans.push(obj.getProduct(opValues[i][0]));
			continue;
		}
		ans.push(null);
	}
	return ans;
}
