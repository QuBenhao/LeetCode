function decodeString(s: string): string {
	const stack: Array<Array<any>> = [];
	let str: string = "";
	let num: number = 0;
	for (let i: number = 0; i < s.length; i++) {
		if (s[i] >= "0" && s[i] <= "9") {
			num = num * 10 + parseInt(s[i]);
		} else if (s[i] === "[") {
			stack.push([str, num]);
			str = "";
			num = 0;
		} else if (s[i] === "]") {
			const [lastStr, lastNum] = stack.pop();
			str = lastStr + str.repeat(lastNum);
		} else {
			str += s[i];
		}
	}
	return str;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(inputValues[0]);
	return decodeString(s);
}
