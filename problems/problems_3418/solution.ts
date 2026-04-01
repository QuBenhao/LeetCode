function maximumAmount(coins: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const coins: number[][] = JSON.parse(inputValues[0]);
	return maximumAmount(coins);
}
