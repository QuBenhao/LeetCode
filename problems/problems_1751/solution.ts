function maxValue(events: number[][], k: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const events: number[][] = JSON.parse(inputValues[0]);
	const k: number = JSON.parse(inputValues[1]);
	return maxValue(events, k);
}
