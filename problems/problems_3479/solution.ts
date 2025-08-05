function numOfUnplacedFruits(fruits: number[], baskets: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const fruits: number[] = JSON.parse(inputValues[0]);
	const baskets: number[] = JSON.parse(inputValues[1]);
	return numOfUnplacedFruits(fruits, baskets);
}
