function clearDigits(s: string): string {
    const st: string[] = [];
	for (const c of s) {
		if (c >= '0' && c <= '9') {
			if (st.length > 0) {
				st.pop();
			}
		} else {
			st.push(c);
		}
	}
	return st.join("");
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(inputValues[0]);
	return clearDigits(s);
}
