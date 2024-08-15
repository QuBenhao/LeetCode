function lengthOfLIS(nums: number[]): number {
    const s: number[] = [];
	for (const num of nums) {
		if (s.length === 0 || num > s[s.length - 1]) {
			s.push(num);
		} else {
			let l: number = 0, r: number = s.length - 1;
			while (l < r) {
				const mid: number = l + ((r - l) >> 1);
				if (s[mid] < num) {
					l = mid + 1;
				} else {
					r = mid;
				}
			}
			s[l] = num;
		}
	}
	return s.length;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return lengthOfLIS(nums);
}
