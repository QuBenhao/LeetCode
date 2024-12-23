function eatenApples(apples: number[], days: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const apples: number[] = JSON.parse(inputValues[0]);
	const days: number[] = JSON.parse(inputValues[1]);
	return eatenApples(apples, days);
}
