function minSubArrayLen(target: number, nums: number[]): number {
	const queue: number[] = [];
	let sum: number = 0;
	const n: number = nums.length;
	let ans: number = n + 1;
	for (let i: number = 0; i < n; i++) {
		queue.push(nums[i]);
		sum += nums[i];
		while (sum >= target) {
			ans = Math.min(ans, queue.length);
			sum -= queue.shift();
		}
	}
	return ans === n + 1 ? 0 : ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const target: number = JSON.parse(inputValues[0]);
	const nums: number[] = JSON.parse(inputValues[1]);
	return minSubArrayLen(target, nums);
}
