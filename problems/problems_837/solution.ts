function new21Game(n: number, k: number, maxPts: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	const k: number = JSON.parse(inputValues[1]);
	const maxPts: number = JSON.parse(inputValues[2]);
	return new21Game(n, k, maxPts);
}
