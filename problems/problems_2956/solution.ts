function findIntersectionValues(nums1: number[], nums2: number[]): number[] {
    const counter: Map<number, number> = new Map<number, number>();
	for (const num of nums2) {
		counter.set(num, (counter.get(num) || 0) + 1);
	}
	const ans: number[] = [0, 0];
	for (const num of nums1) {
		if (!counter.has(num)) {
			continue;
		}
		ans[0]++;
		ans[1] += counter.get(num);
		counter.set(num, 0);
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums1: number[] = JSON.parse(inputValues[0]);
	const nums2: number[] = JSON.parse(inputValues[1]);
	return findIntersectionValues(nums1, nums2);
}
