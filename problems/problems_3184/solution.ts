function countCompleteDayPairs(hours: number[]): number {
    const hs: number[] = new Array(24).fill(0);
	for (const h of hours) {
		hs[h % 24]++;
	}
	let res: number = 0;
	for (let i: number = 1; i < 12; i++) {
		res += hs[i] * hs[24 - i];
	}
	res += hs[0] * (hs[0] - 1) / 2;
	res += hs[12] * (hs[12] - 1) / 2;
	return res;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const hours: number[] = JSON.parse(inputValues[0]);
	return countCompleteDayPairs(hours);
}
