function countQuadruplets(nums: number[]): number {
	const n: number = nums.length;
	let cnt4: number = 0;
	const cn3: number[] = new Array(n).fill(0);
	for (let l: number = 2; l < n; l++) {
		let cnt2: number = 0;
		for (let j: number = 0; j < l; j++) {
			if (nums[j] < nums[l]) {
				cnt4 += cn3[j];
				cnt2++;
			} else {
				cn3[j] += cnt2;
			}
		}
	}
	return cnt4;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return countQuadruplets(nums);
}
