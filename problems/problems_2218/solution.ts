function maxValueOfCoins(piles: number[][], k: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const piles: number[][] = JSON.parse(inputValues[0]);
	const k: number = JSON.parse(inputValues[1]);
	return maxValueOfCoins(piles, k);
}
