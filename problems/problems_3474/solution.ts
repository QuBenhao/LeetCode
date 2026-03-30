function generateString(str1: string, str2: string): string {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const str1: string = JSON.parse(inputValues[0]);
	const str2: string = JSON.parse(inputValues[1]);
	return generateString(str1, str2);
}
