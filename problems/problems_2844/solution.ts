function minimumOperations(num: string): number {
	const n: number = num.length;
	let zero: boolean = false, five: boolean = false;
	for (let i: number = n - 1; i >= 0; i--) {
		const c: string = num[i];
		if (zero && (c === "0" || c === "5") || five && (c === "2" || c === "7")) {
			return n - i - 2;
		}
		if (c === "0") {
			zero = true;
		}
		if (c === "5") {
			five = true;
		}
	}
	return zero ? n - 1 : n;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const num: string = JSON.parse(inputValues[0]);
	return minimumOperations(num);
}
