function addedInteger(nums1: number[], nums2: number[]): number {
    let m1: number = nums1[0], m2: number = nums2[0];
	for (const v of nums1) {
		m1 = Math.min(m1, v);
	}
	for (const v of nums2) {
		m2 = Math.min(m2, v);
	}
	return m2 - m1;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums1: number[] = JSON.parse(inputValues[0]);
	const nums2: number[] = JSON.parse(inputValues[1]);
	return addedInteger(nums1, nums2);
}
