function maxSlidingWindow(nums: number[], k: number): number[] {
    const q: number[] = [];
	const ans: number[] = [];
	for (let i: number = 0; i < nums.length; i++) {
		while (q.length > 0 && nums[q[q.length - 1]] <= nums[i]) {
			q.pop();
		}
		q.push(i);
		if (i >= k + q[0]) {
			q.shift();
		}
		if (i >= k - 1) {
			ans.push(nums[q[0]]);
		}
 	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	const k: number = JSON.parse(inputValues[1]);
	return maxSlidingWindow(nums, k);
}
