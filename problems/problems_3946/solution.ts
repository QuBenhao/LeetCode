function maximumSaleItems(items: number[][], budget: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const items: number[][] = JSON.parse(inputValues[0]);
	const budget: number = JSON.parse(inputValues[1]);
	return maximumSaleItems(items, budget);
}
