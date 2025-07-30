function doesValidArrayExist(derived: number[]): boolean {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const derived: number[] = JSON.parse(inputValues[0]);
	return doesValidArrayExist(derived);
}
