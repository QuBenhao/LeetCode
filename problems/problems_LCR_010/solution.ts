function subarraySum(nums: number[], k: number): number {
	let ans: number = 0, sum: number = 0;
	const map: Map<number, number> = new Map<number, number>();
	map.set(0, 1);
	for (let i: number = 0; i < nums.length; i++) {
		sum += nums[i];
		if (map.has(sum - k)) {
			ans += map.get(sum - k);
		}
		map.set(sum, (map.get(sum) || 0) + 1);
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	const k: number = JSON.parse(inputValues[1]);
	return subarraySum(nums, k);
}
