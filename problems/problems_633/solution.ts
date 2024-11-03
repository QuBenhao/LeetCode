function judgeSquareSum(c: number): boolean {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const c: number = JSON.parse(inputValues[0]);
	return judgeSquareSum(c);
}
