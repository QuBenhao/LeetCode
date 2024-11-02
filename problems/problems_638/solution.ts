function shoppingOffers(price: number[], special: number[][], needs: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const price: number[] = JSON.parse(inputValues[0]);
	const special: number[][] = JSON.parse(inputValues[1]);
	const needs: number[] = JSON.parse(inputValues[2]);
	return shoppingOffers(price, special, needs);
}
