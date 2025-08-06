function maxCollectedFruits(fruits: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const fruits: number[][] = JSON.parse(inputValues[0]);
	return maxCollectedFruits(fruits);
}
