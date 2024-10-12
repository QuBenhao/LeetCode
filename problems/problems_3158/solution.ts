function duplicateNumbersXOR(nums: number[]): number {
    let ans: number = 0;
	const explored: Set<number> = new Set<number>();
	for (const num of nums) {
		if (explored.has(num)) {
			ans ^= num;
		} else {
			explored.add(num);
		}
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return duplicateNumbersXOR(nums);
}
