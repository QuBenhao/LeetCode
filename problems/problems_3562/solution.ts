function maxProfit(n: number, present: number[], future: number[], hierarchy: number[][], budget: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	const present: number[] = JSON.parse(inputValues[1]);
	const future: number[] = JSON.parse(inputValues[2]);
	const hierarchy: number[][] = JSON.parse(inputValues[3]);
	const budget: number = JSON.parse(inputValues[4]);
	return maxProfit(n, present, future, hierarchy, budget);
}
