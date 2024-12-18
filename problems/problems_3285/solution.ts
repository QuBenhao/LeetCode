function stableMountains(height: number[], threshold: number): number[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const height: number[] = JSON.parse(inputValues[0]);
	const threshold: number = JSON.parse(inputValues[1]);
	return stableMountains(height, threshold);
}
