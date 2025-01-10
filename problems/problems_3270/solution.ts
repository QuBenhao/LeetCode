function generateKey(num1: number, num2: number, num3: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const num1: number = JSON.parse(inputValues[0]);
	const num2: number = JSON.parse(inputValues[1]);
	const num3: number = JSON.parse(inputValues[2]);
	return generateKey(num1, num2, num3);
}
