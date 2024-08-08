function minimumAddedInteger(nums1: number[], nums2: number[]): number {
    nums1.sort((a, b) => a - b);
	nums2.sort((a, b) => a - b);
	out:
	for (let i: number = 2; i >= 1; i--) {
		const diff: number = nums2[0] - nums1[i];
		let quota: number = 2 - i, idx: number = i + 1;
		for (let j: number = 1; j < nums2.length; j++) {
			while (nums2[j] - nums1[idx] != diff) {
				if (quota-- === 0) {
					continue out;
				}
				idx++;
			}
			idx++;
		}
		return diff;
	}
	return nums2[0] - nums1[0];
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums1: number[] = JSON.parse(inputValues[0]);
	const nums2: number[] = JSON.parse(inputValues[1]);
	return minimumAddedInteger(nums1, nums2);
}
