function merge(intervals: number[][]): number[][] {
	const result: number[][] = [];
	intervals.sort((a, b) => a[0] - b[0]);
	for (const interval of intervals) {
		if (result.length === 0 || result[result.length - 1][1] < interval[0]) {
			result.push(interval);
		} else {
			result[result.length - 1][1] = Math.max(result[result.length - 1][1], interval[1]);
		}
	}
	return result;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const intervals: number[][] = JSON.parse(inputValues[0]);
	return merge(intervals);
}
