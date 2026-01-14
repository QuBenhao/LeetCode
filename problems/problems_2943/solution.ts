function maximizeSquareHoleArea(n: number, m: number, hBars: number[], vBars: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	const m: number = JSON.parse(inputValues[1]);
	const hBars: number[] = JSON.parse(inputValues[2]);
	const vBars: number[] = JSON.parse(inputValues[3]);
	return maximizeSquareHoleArea(n, m, hBars, vBars);
}
