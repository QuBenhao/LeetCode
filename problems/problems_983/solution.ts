function mincostTickets(days: number[], costs: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const days: number[] = JSON.parse(inputValues[0]);
	const costs: number[] = JSON.parse(inputValues[1]);
	return mincostTickets(days, costs);
}
