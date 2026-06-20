function maxIceCream(costs: number[], coins: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const costs: number[] = JSON.parse(inputValues[0]);
	const coins: number = JSON.parse(inputValues[1]);
	return maxIceCream(costs, coins);
}
