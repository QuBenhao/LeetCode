class BrowserHistory {
    b: string[];
    f: string[];
    constructor(homepage: string) {
        this.b = [homepage];
        this.f = [];
    }

    visit(url: string): void {
        this.b.push(url);
        while (this.f.length > 0) {
            this.f.pop()
        }
    }

    back(steps: number): string {
        steps = Math.min(steps, this.b.length - 1);
        for (let i: number = 0; i < steps; i++) {
            this.f.push(this.b.pop()!!);
        }
        return this.b[this.b.length - 1];
    }

    forward(steps: number): string {
        steps = Math.min(steps, this.f.length);
        for (let i: number = 0; i < steps; i++) {
            this.b.push(this.f.pop()!!);
        }
        return this.b[this.b.length - 1];
    }
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * var obj = new BrowserHistory(homepage)
 * obj.visit(url)
 * var param_2 = obj.back(steps)
 * var param_3 = obj.forward(steps)
 */

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const operators: string[] = JSON.parse(splits[0]);
	const values: any[][] = JSON.parse(splits[1]);
	const ans: any[] = [null];
	const obj: BrowserHistory = new BrowserHistory(values[0][0]);
	for (let i: number = 1; i < operators.length; i++) {
		if (operators[i] == "visit") {
			obj.visit(values[i][0]);
			ans.push(null);
			continue;
		}
		if (operators[i] == "back") {
			ans.push(obj.back(values[i][0]));
			continue;
		}
		if (operators[i] == "forward") {
			ans.push(obj.forward(values[i][0]));
			continue;
		}
		ans.push(null);
	}
	return ans;
}
