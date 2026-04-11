function minimumDistance(nums: number[]): number {
    let ans = Number.MAX_SAFE_INTEGER;
    const record: Map<number, number[]> = new Map();
    for (let k = 0; k < nums.length; k++) {
        const num = nums[k];
        if (!record.has(num)) {
            record.set(num, []);
        }
        record.get(num)!.push(k);
        const indices = record.get(num)!;
        if (indices.length > 2) {
            const i = indices[indices.length - 3];
            ans = Math.min(ans, (k - i) * 2);
        }
    }
    return ans === Number.MAX_SAFE_INTEGER ? -1 : ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return minimumDistance(nums);
}
