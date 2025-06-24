function kthSmallestProduct(nums1: number[], nums2: number[], k: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums1: number[] = JSON.parse(inputValues[0]);
	const nums2: number[] = JSON.parse(inputValues[1]);
	const k: number = JSON.parse(inputValues[2]);
	return kthSmallestProduct(nums1, nums2, k);
}
