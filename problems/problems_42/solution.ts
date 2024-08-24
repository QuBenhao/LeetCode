function trap(height: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const height: number[] = JSON.parse(inputValues[0]);
	return trap(height);
}
