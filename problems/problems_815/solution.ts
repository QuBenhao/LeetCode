function numBusesToDestination(routes: number[][], source: number, target: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const routes: number[][] = JSON.parse(inputValues[0]);
	const source: number = JSON.parse(inputValues[1]);
	const target: number = JSON.parse(inputValues[2]);
	return numBusesToDestination(routes, source, target);
}
