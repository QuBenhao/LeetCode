function maxScoreSightseeingPair(values: number[]): number {
	let ans: number = 0, left: number = values[0];
	for (let i: number = 1; i < values.length; i++) {
		ans = Math.max(ans, left + values[i] - i);
		left = Math.max(left, values[i] + i);
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const values: number[] = JSON.parse(inputValues[0]);
	return maxScoreSightseeingPair(values);
}
