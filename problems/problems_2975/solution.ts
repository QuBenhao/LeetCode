function maximizeSquareArea(m: number, n: number, hFences: number[], vFences: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const m: number = JSON.parse(inputValues[0]);
	const n: number = JSON.parse(inputValues[1]);
	const hFences: number[] = JSON.parse(inputValues[2]);
	const vFences: number[] = JSON.parse(inputValues[3]);
	return maximizeSquareArea(m, n, hFences, vFences);
}
