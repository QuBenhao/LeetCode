function splitNum(num: number): number {
    let nums: Array<number> = [];
	while (num > 0) {
		const r: number = num % 10;
		if (r !== 0) {
			nums.push(r);
		}
		num = Math.floor(num / 10);
	}
	nums.sort((a, b) => a - b);
	let a: number = 0, b: number = 0;
	for (let i: number = 0; i < nums.length; i++) {
		if (i % 2 === 0) {
			a = a * 10 + nums[i];
		} else {
			b = b * 10 + nums[i];
		}
	}
	return a + b;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const num: number = JSON.parse(inputValues[0]);
	return splitNum(num);
}
