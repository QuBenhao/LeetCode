function countAlternatingSubarrays(nums: number[]): number {
    let ans: number = 0, cnt: number = 0;
	for (let i: number = 0; i < nums.length; i++) {
		if (i == 0 || nums[i] != nums[i - 1]) {
			cnt++;
		} else {
			cnt = 1;
		}
		ans += cnt;
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return countAlternatingSubarrays(nums);
}
