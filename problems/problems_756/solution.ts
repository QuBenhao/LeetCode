function pyramidTransition(bottom: string, allowed: string[]): boolean {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const bottom: string = JSON.parse(inputValues[0]);
	const allowed: string[] = JSON.parse(inputValues[1]);
	return pyramidTransition(bottom, allowed);
}
