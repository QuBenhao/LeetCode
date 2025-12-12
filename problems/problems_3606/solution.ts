function validateCoupons(code: string[], businessLine: string[], isActive: boolean[]): string[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const code: string[] = JSON.parse(inputValues[0]);
	const businessLine: string[] = JSON.parse(inputValues[1]);
	const isActive: boolean[] = JSON.parse(inputValues[2]);
	return validateCoupons(code, businessLine, isActive);
}
