function totalWaviness(num1: number, num2: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const num1: number = JSON.parse(inputValues[0]);
	const num2: number = JSON.parse(inputValues[1]);
	return totalWaviness(num1, num2);
}
