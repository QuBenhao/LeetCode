function minimumLevels(possible: number[]): number {
    let s: number = possible.map((x: number) => x === 0 ? -1 : x).reduce((a: number, b: number) => a + b);
	for (let i: number = 0, pre: number = 0; i < possible.length - 1; i++) {
		pre += possible[i] === 0 ? -1 : possible[i];
		if (pre * 2 > s) {
			return i + 1;
		}
	}
	return -1;
};

export function Solve(inputJsonElement: string): any {
    const inputValues: string[] = inputJsonElement.split("\n");
    const possible: number[] = JSON.parse(inputValues[0]);
    return minimumLevels(possible);
}
