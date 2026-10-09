function minSumSquareDiff(nums1: number[], nums2: number[], k1: number, k2: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums1: number[] = JSON.parse(inputValues[0]);
	const nums2: number[] = JSON.parse(inputValues[1]);
	const k1: number = JSON.parse(inputValues[2]);
	const k2: number = JSON.parse(inputValues[3]);
	return minSumSquareDiff(nums1, nums2, k1, k2);
}
