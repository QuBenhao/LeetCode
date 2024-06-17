function twoSum(nums: number[], target: number): number[] {
    const map: Map<number, any> = new Map();
	for (let i = 0; i < nums.length; i++) {
		if (map.has(target - nums[i])) {
			return [map.get(target - nums[i]), i]
		}
		map.set(nums[i], i)
	}
	return [-1, -1]
};

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(splits[0]);
	const target: number = JSON.parse(splits[1]);
	return twoSum(nums, target);
}
