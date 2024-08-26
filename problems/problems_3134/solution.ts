function medianOfUniquenessArray(nums: number[]): number {
    const n: number = nums.length;
	const k: number = Math.floor((n * (n + 1) / 2 + 1) / 2);

	const check = (x: number): boolean => {
		const freq: Map<number, number> = new Map();
		let cnt: number = 0;
		for (let l: number = 0, r: number = 0; r < n; r++) {
			freq.set(nums[r], (freq.get(nums[r]) || 0) + 1);
			while (freq.size > x) {
				freq.set(nums[l], freq.get(nums[l]) - 1);
				if (freq.get(nums[l]) == 0) {
					freq.delete(nums[l]);
				}
				l++;
			}
			cnt += r - l + 1;
			if (cnt >= k) {
				return true;
			}
		}
		return false;
	};

	let left: number = 1, right: number = n;
	while (left < right) {
		const mid: number = left + Math.floor((right - left) / 2);
		if (check(mid)) {
			right = mid;
		} else {
			left = mid + 1;
		}
	}
	return left;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return medianOfUniquenessArray(nums);
}
