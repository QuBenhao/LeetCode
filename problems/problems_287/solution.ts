function findDuplicate(nums: number[]): number {
    let slow: number = 0, fast: number = 0;
	do {
		slow = nums[slow];
		fast = nums[nums[fast]];
	} while (slow != fast);
	slow = 0;
	while (slow != fast) {
		slow = nums[slow];
		fast = nums[fast];
	}
	return slow;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return findDuplicate(nums);
}
