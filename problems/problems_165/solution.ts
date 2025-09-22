function compareVersion(version1: string, version2: string): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const version1: string = JSON.parse(inputValues[0]);
	const version2: string = JSON.parse(inputValues[1]);
	return compareVersion(version1, version2);
}
