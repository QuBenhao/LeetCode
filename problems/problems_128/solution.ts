function longestConsecutive(nums: number[]): number {
	const map: Map<number, number> = new Map<number, number>();
	let result: number = 0;
	for (const num of nums) {
		if (!map.has(num)) {
			const left: number = map.get(num - 1) || 0;
			const right: number = map.get(num + 1) || 0;
			const sum: number = left + right + 1;
			map.set(num, sum);
			map.set(num - left, sum);
			map.set(num + right, sum);
			result = Math.max(result, sum);
		}
	}
	return result;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return longestConsecutive(nums);
}
