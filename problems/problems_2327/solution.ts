function peopleAwareOfSecret(n: number, delay: number, forget: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	const delay: number = JSON.parse(inputValues[1]);
	const forget: number = JSON.parse(inputValues[2]);
	return peopleAwareOfSecret(n, delay, forget);
}
