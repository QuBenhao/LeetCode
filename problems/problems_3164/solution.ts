function numberOfPairs(nums1: number[], nums2: number[], k: number): number {
    const counter: Map<number, number> = new Map<number, number>();
	for (let num of nums1) {
		if (num % k !== 0) {
			continue;
		}
		num /= k;
		for (let i: number = 1; i * i <= num; i++) {
			if (num % i === 0) {
				counter.set(i, (counter.get(i) || 0) + 1);
				if (i * i !== num) {
					counter.set(num / i, (counter.get(num / i) || 0) + 1);
				}
			}
		}
	}
	let result: number = 0;
	for (const num of nums2) {
		result += counter.get(num) || 0;
	}
	return result;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums1: number[] = JSON.parse(inputValues[0]);
	const nums2: number[] = JSON.parse(inputValues[1]);
	const k: number = JSON.parse(inputValues[2]);
	return numberOfPairs(nums1, nums2, k);
}
