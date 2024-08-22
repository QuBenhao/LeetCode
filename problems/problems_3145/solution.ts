function findProductsOfElements(queries: number[][]): number[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const queries: number[][] = JSON.parse(inputValues[0]);
	return findProductsOfElements(queries);
}
