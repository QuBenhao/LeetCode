function bestClosingTime(customers: string): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const customers: string = JSON.parse(inputValues[0]);
	return bestClosingTime(customers);
}
