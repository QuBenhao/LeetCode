function minimumSeconds(nums: number[]): number {
	const n: number = nums.length;
	const idxMap: Map<number, Array<number>> = new Map();
	for (let i: number = 0; i < n; i++) {
		if (!idxMap.has(nums[i])) {
			idxMap.set(nums[i], []);
		}
		idxMap.get(nums[i]).push(i);
	}
	let ans: number = n;
	// @ts-ignore
	for (const idxes of idxMap.values()) {
		if (idxes.length === 1) {
			continue;
		}
		let cur: number = idxes[0] + n - idxes[idxes.length - 1];
		for (let i: number = 1; i < idxes.length; i++) {
			cur = Math.max(cur, idxes[i] - idxes[i - 1]);
		}
		ans = Math.min(ans, cur);
	}
	return ans >> 1;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return minimumSeconds(nums);
}
