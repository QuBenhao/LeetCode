function addBinary(a: string, b: string): string {
	if (a.length < b.length) {
		return addBinary(b, a);
	}
	const result: string[] = [];
	let carry: number = 0;
	const d: number = a.length - b.length;
	for (let i: number = a.length - 1; i >= 0; i--) {
		const sum: number = parseInt(a[i]) + (i - d >= 0 ? parseInt(b[i - d]) : 0) + carry;
		result.push((sum % 2).toString());
		carry = Math.floor(sum / 2);
	}
	if (carry) {
		result.push("1");
	}
	return result.reverse().join("");
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const a: string = JSON.parse(inputValues[0]);
	const b: string = JSON.parse(inputValues[1]);
	return addBinary(a, b);
}
