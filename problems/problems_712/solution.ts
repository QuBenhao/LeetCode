function minimumDeleteSum(s1: string, s2: string): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s1: string = JSON.parse(inputValues[0]);
	const s2: string = JSON.parse(inputValues[1]);
	return minimumDeleteSum(s1, s2);
}
