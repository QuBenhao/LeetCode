function convertDateToBinary(date: string): string {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const date: string = JSON.parse(inputValues[0]);
	return convertDateToBinary(date);
}
