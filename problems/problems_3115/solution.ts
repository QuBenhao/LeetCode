function maximumPrimeDifference(nums: number[]): number {
    const isPrime = (n: number): boolean => {
		for (let i: number = 2; i * i <= n; i++) {
			if (n % i === 0) {
				return false;
			}
		}
		return n >= 2;
	}
	let left: number = 0, right: number = nums.length - 1;
	while (left < right && !isPrime(nums[left])) {
		left++;
	}
	while (left < right && !isPrime(nums[right])) {
		right--;
	}
	return right - left;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return maximumPrimeDifference(nums);
}
