function minimumCost(source: string, target: string, original: string[], changed: string[], cost: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const source: string = JSON.parse(inputValues[0]);
	const target: string = JSON.parse(inputValues[1]);
	const original: string[] = JSON.parse(inputValues[2]);
	const changed: string[] = JSON.parse(inputValues[3]);
	const cost: number[] = JSON.parse(inputValues[4]);
	return minimumCost(source, target, original, changed, cost);
}
