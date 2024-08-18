function checkRecord(s: string): boolean {
    return !s.includes("LLL") && s.indexOf("A") == s.lastIndexOf("A");
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(inputValues[0]);
	return checkRecord(s);
}
